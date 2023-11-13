import pygame, sys, random

width, height = 800, 600
title = "battle"
battle_background = pygame.image.load("battle.png")
battle_background = pygame.transform.scale(battle_background, (width, height))
demon = pygame.image.load("demon.png")
demon = pygame.transform.scale(demon, (300, 300))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(battle_background, (0, 0))
    screen.blit(demon, ((width/2) - 225, (height/2) - 140))
    pygame.display.flip()
    clock.tick(60)
