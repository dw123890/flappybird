import pygame, random
from pygame.locals import *
from nyancat import nyancat
from pipes import Platform

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (width, height))

#set up game variables
platforms = pygame.sprite.Group()
startPos = (width/8, height/2)
Player = nyancat(startPos)
GapSize = 200
Ticks = 0
loopCount = 0
score = 1

def lose():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You died", True, (255, 0, 0))
    text_rect = text.get_rect()
    text.rect.center = (width/2, height/2)
    while True:
        clock.tick(60)
        screen.fiol(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    platforms.empty()
                    Player.reset(startPos)
                    return

def main():
    global loopCount
    while True:
        clock.tick(60)
        if loopCount % 90 == 0:
            toppos = random.randint(0, height/2) -400
            platforms.add(Platform((width + 100, toppos + GapSize + 800)))
            platforms.add(Platform((width + 100, toppos),True))
        for event in pygame.event.get():
            if event in pygame.event.get():
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Player.speed[1] = -10


        screen.fill(color)
        Player.update()
        platforms.update()
        gets_hit = pygame.sprite.spritecollide(Player, platforms, False)\
                    or Player.rect.center[1] > height
        screen.blit(background, [0, 0])
        platforms.draw(screen)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()
        loopCount += 1

        if gets_hit:
            lose()


if __name__ == '__main__':
    main()


