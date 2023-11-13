# Imports used in program
import random, pygame, sys

# Constants throughout program
width, height = 800, 600
player_width, player_height = 384, 550
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (800, 600))
try:
    player_image = pygame.image.load("playermovedownbase.png")
except:
    print("no image in directory")
player_image = pygame.transform.scale(player_image, (64, 64))
title = "JABRPG"
battle = False
moving = False
try:
    battle_background = pygame.image.load("battle.png")
except:
    print("no image in directory")
battle_background = pygame.transform.scale(battle_background, (width, height))
size_x = 64
size_y = 64
time = 0.0

# mobs
try:
    demon = pygame.image.load("demon.png")
except:
    print("no image in directory")
demon = pygame.transform.scale(demon, (300, 300))

# pygame initialization
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()


# Class: Window
# Description: This class determines which window will be displayed on the screen, it will either
# display the world screen or battle screen
class Window:
    def __int__(self):
        self.state = 'world'

    # Function: World
    # Description: This has the functions that occur in the world screen, where the user can move
    # around with keyboard inputs
    # Inputs: User movements with wasd
    # Output: GUI displayed with character and movement
    def world():
        global player_image
        global moving
        global image
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Test for key presses on keyboard from user
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
                player_image = pygame.image.load("playermovedownbase.png")
                player_image = pygame.transform.scale(player_image, (size_x, size_y))
            if player.up_pressed:
                player_image = pygame.image.load("playermoveupbase.png")
                player_image = pygame.transform.scale(player_image, (size_x, size_y))
            if player.left_pressed:
                player_image = pygame.image.load("playermoveleftbase.png")
                player_image = pygame.transform.scale(player_image, (size_x, size_y))
            if player.right_pressed:
                player_image = pygame.image.load("playermoverightbase.png")
                player_image = pygame.transform.scale(player_image, (size_x, size_y))

        # Draw background and character onto screen
        screen.blit(background, (0, 0))
        screen.blit(player_image, (player.x, player.y))

        # Run the update function
        player.update()
        pygame.display.flip()

    # Function: Battle
    # Description: This has the functions that occur in the battle screen, where the enemy appears on screen
    # Output: GUI displayed with enemy
    def battle():
        global battle
        global time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(battle_background, (0, 0))
        screen.blit(demon, ((width / 2) - 170, (height / 2) - 140))

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        battle = False
                        running()

                pygame.display.flip()


# Class: Player
# Description: This class is used to create the player as an object.
# Inputs: The width and height of character passed as parabolas
class Player:
    # Function: __init__
    # Description: The basic structure needed to create object in pygame
    # Input: The coordinates of the character on screen
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

    # Function: update
    # Description: The change in the character's location are changed to match with movement made through user input
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

        # Creating a border, preventing the character from moving if it reaches the edge of the screen
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
pygame.mouse.set_visible(False)


# Main Loop

# Function: running
# Description: The main aprt of the program which begins running the code determining which window
# should be displayed when
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
            # Reset all values
            time = 0.0
            player.left_pressed = False
            player.right_pressed = False
            player.down_pressed = False
            player.up_pressed = False
            game_state.battle()

        clock.tick(100)


running()
