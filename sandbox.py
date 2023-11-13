# Imports
import random, pygame, sys

# Constants
mobImages = []
width, height = 800, 600
player_width, player_height = 384, 550
background = pygame.image.load("gameattempt/Assets/bg.png")
background = pygame.transform.scale(background, (800, 600))
picture = pygame.image.load("gameattempt/Assets/playermovedownbase.png")
picture = pygame.transform.scale(picture, (64, 64))
title = "JABRPG"
battle = False
moving = False
battle_background = pygame.image.load("gameattempt/Assets/battle.png")
battle_background = pygame.transform.scale(battle_background, (width, height))
time = 0.0

# mobs
demon = pygame.image.load("gameattempt/Assets/demon.png")
demon = pygame.transform.scale(demon, (300, 300))
mobImages.append(demon)
dragon = pygame.image.load("gameattempt/Assets/dragon.png")
dragon = pygame.transform.scale(dragon, (300, 300))
mobImages.append(dragon)
ratman = pygame.image.load("gameattempt/Assets/ratman.png")
ratman = pygame.transform.scale(ratman, (300, 300))
mobImages.append(ratman)
mrlion = pygame.image.load("gameattempt/Assets/mrlion.png")
mrlion = pygame.transform.scale(mrlion, (300, 300))
mobImages.append(mrlion)
octopus = pygame.image.load("gameattempt/Assets/octopus.png")
octopus = pygame.transform.scale(octopus, (300, 300))
mobImages.append(octopus)
# pygame initialization
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()
size_x = 64
size_y = 64


class Window:
    def __int__(self):
        self.state = 'world'

    def world():
        global picture
        global moving
        global image
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Test for key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.left_pressed = True
                    player.right_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False
                    moving = True
                if event.key == pygame.K_d:
                    player.right_pressed = True
                    player.left_pressed = False
                    player.up_pressed = False
                    player.down_pressed = False
                    moving = True
                if event.key == pygame.K_w:
                    player.up_pressed = True
                    player.right_pressed = False
                    player.left_pressed = False
                    player.down_pressed = False
                    moving = True
                if event.key == pygame.K_s:
                    player.down_pressed = True
                    player.right_pressed = False
                    player.up_pressed = False
                    player.left_pressed = False
                    moving = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.left_pressed = False
                    moving = False
                if event.key == pygame.K_d:
                    player.right_pressed = False
                    moving = False
                if event.key == pygame.K_w:
                    player.up_pressed = False
                    moving = False
                if event.key == pygame.K_s:
                    player.down_pressed = False
                    moving = False

            if player.down_pressed:
                picture = pygame.image.load("gameattempt/Assets/playermovedownbase.png")
                picture = pygame.transform.scale(picture, (size_x, size_y))
            if player.up_pressed:
                picture = pygame.image.load("gameattempt/Assets/playermoveupbase.png")
                picture = pygame.transform.scale(picture, (size_x, size_y))
            if player.left_pressed:
                picture = pygame.image.load("gameattempt/Assets/playermoveleftbase.png")
                picture = pygame.transform.scale(picture, (size_x, size_y))
            if player.right_pressed:
                picture = pygame.image.load("gameattempt/Assets/playermoverightbase.png")
                picture = pygame.transform.scale(picture, (size_x, size_y))

        # Draw
        screen.blit(background, (0, 0))
        screen.blit(picture, (player.x, player.y))

        # update
        player.update()
        pygame.display.flip()

    def battle():
        global battle
        global time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(battle_background, (0, 0))
        screen.blit(random.choice(mobImages), ((width / 2) - 170, (height / 2) - 140))
        pygame.display.flip()

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        battle = False

                        running()
                        break


# Player Class
class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (255, 255, 255)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2.5

    # change position on the player
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        # Creating a border
        if self.x < 0:
            self.x = 0
        if self.x > width - 64:
            self.x = width - 64
        if self.y < 80:
            self.y = 80
        if self.y > height - 64:
            self.y = height - 64


# Player Initialization
player = Player(player_width, player_height)
game_state = Window
# Make mouse invisible
pygame.mouse.set_visible(False)


# Main Loop

def running():
    global time
    global battle
    global moving
    battle = False
    while True:
        if moving:
            time += 10
        if moving and time > 1000:
            number = random.randint(1, 10)
            if number == 1:
                battle = True

        if not battle:
            game_state.world()
        if battle:
            time = 0.0
            player.left_pressed = False
            player.right_pressed = False
            player.down_pressed = False
            player.up_pressed = False
            game_state.battle()

        clock.tick(100)


running()
