import pygame
import sys

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
colour = (0, 200, 150)

screen.fill(colour)
pygame.display.flip()

base_font = pygame.font.Font(None, 32)
username = ''

colour_active = pygame.Color(0, 200, 100)

colour_passive = pygame.Color(255, 255, 255)

colour = colour_passive

active = False

input_rect = pygame.Rect(200, 200, 140, 32)

pygame.display.set_caption("test window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username = username[:-1]

            elif event.key == pygame.K_RETURN:
                f = open("login.txt", "a")
                f.write(username)

            else:
                username += event.unicode

    if active:
        color = colour_active
    else:
        color = colour_passive

    pygame.draw.rect(screen, color, input_rect)

    text_surface = base_font.render(username, True, (255, 255, 255))

    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    input_rect.w = max(100, text_surface.get_width()+10)

    clock.tick(60)
