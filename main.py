import pygame, random
from pygame.locals import *
from nyancat import nyancat
from pipes import Platform
from score import Score

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
background = pygame.image.load('backdrop.jpeg')
background = pygame.transform.scale(background, (width, height))
background2 = pygame.image.load('nyancat.gif')
#background2 = pygame.transform.scale(background2, (width, height))



#set up game variables
platforms = pygame.sprite.Group()
scorecounters = pygame.sprite.Group()
startPos = (width/8, height/2)
Player = nyancat(startPos)
GapSize = 200
Ticks = 0
loopCount = 0
score = 0

def lose():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You died", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    platforms.empty()
                    Player.reset(startPos)
                    return

def displayScore():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (100, 50)
    screen.blit(text, text_rect)

def main():
    global loopCount, score
    while True:
        clock.tick(60)
        if loopCount % 90 == 0:
            toppos = random.randint(0, height/2) -400
            platforms.add(Platform((width + 100, toppos + GapSize + 800)))
            platforms.add(Platform((width + 100, toppos),True))
            scorecounters.add(Score((width + 100, 0)))

        for event in pygame.event.get():
            if event in pygame.event.get():
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Player.speed[1] = -10


        screen.fill(color)
        Player.update()
        platforms.update()
        scorecounters.update()
        gets_hit = pygame.sprite.spritecollide(Player, platforms, False)\
                    or Player.rect.center[1] > height
        score_hit = pygame.sprite.spritecollide(Player, scorecounters, True)
        screen.blit(background, [0, 0])
        screen.blit(background2, [500, 200])
        platforms.draw(screen)
        scorecounters.draw(screen)
        screen.blit(Player.image, Player.rect)
        displayScore()
        pygame.display.flip()
        loopCount += 1

        if gets_hit:
            lose()
            score = 0

        if score_hit:
            score+=1


if __name__ == '__main__':
    main()


