from pygame.locals import *
import pygame
import sys
from InitScreen import InitScreen 

'''
This script is a pygame app for recreate Space Invaders.
@Author: Alejandro 'Xiph' Lozano
@Date: February of 2019
'''

#[Global Variables]
HEIGHT = 640
WIDTH = 480
SCREEN_X_CENTER = WIDTH / 2
SCREEN_Y_CENTER = HEIGHT / 2

initialScreen = True
counter = 0
direction = 1

#[Pygame Setups]
pygame.init() 
pygame.display.set_caption("Space Invaders") #Sets the window title
fpsClock = pygame.time.Clock()

#[Class instances]
InitialScreen = InitScreen()

#[Gameplay variables]
player_movement = 5
enemies_movement = player_movement // 2 
enemies_rows = 3
enemies_columns = 5

#[Fonts initialitation]
font_16 = pygame.font.Font("PressStart2P.ttf", 16)
font_18 = pygame.font.Font("PressStart2P.ttf", 18)
font_35 = pygame.font.Font("PressStart2P.ttf", 35)

#Stores "spriteID.txt" content in a list. Then, evaluates the ID for loading sprites.
spriteID = open("spritesID.txt").readlines()

while counter < len(spriteID):
    line = spriteID[counter].split()
    SRF = 4 #Sprite Redimension Factor: How much will the sprites be downscaled. 

    if line[0] == "player":
        print("Loading player file: " + line[1])
        player = pygame.image.load(line[1])
        PLAYER_SIZE_X, PLAYER_SIZE_Y = player.get_rect().size[0], \
                                        player.get_rect().size[1]
        print (PLAYER_SIZE_X, PLAYER_SIZE_Y)
        player = pygame.transform.scale(player, (PLAYER_SIZE_X//2, PLAYER_SIZE_Y//2))
        PLAYER_SIZE_X, PLAYER_SIZE_Y = player.get_rect().size[0], \
                                        player.get_rect().size[1] 
    
    elif line[0] == "enemy1_1":
        print("Loading enemy1_1 file: " + line[1]) 
        enemy1_1 = pygame.image.load(line[1])
        ENEMY1_1_SIZE_X, ENEMY1_1_SIZE_Y =  enemy1_1.get_rect().size[0], \
                                            enemy1_1.get_rect().size[1]
        print (ENEMY1_1_SIZE_X, ENEMY1_1_SIZE_Y)
        enemy1_1 = pygame.transform.scale(enemy1_1, (ENEMY1_1_SIZE_X//SRF, ENEMY1_1_SIZE_Y//SRF))
        ENEMY1_1_SIZE_X, ENEMY1_1_SIZE_Y =  enemy1_1.get_rect().size[0], \
                                            enemy1_1.get_rect().size[1]
        
    elif line[0] == "enemy1_2":
        print("Loading enemy1_2 file: " + line[1])
        enemy1_2 = pygame.image.load(line[1])
        ENEMY1_2_SIZE_X, ENEMY1_2_SIZE_Y =  enemy1_2.get_rect().size[0], \
                                            enemy1_2.get_rect().size[1]
        enemy1_2 = pygame.transform.scale(enemy1_2, (ENEMY1_2_SIZE_X//SRF, ENEMY1_2_SIZE_Y//SRF))
        ENEMY1_2_SIZE_X, ENEMY1_2_SIZE_Y =  enemy1_2.get_rect().size[0], \
                                            enemy1_2.get_rect().size[1]

    elif line[0] == "enemy2_1":
        print("Loading enemy2_1 file: " + line[1])
        enemy2_1 = pygame.image.load(line[1])
        ENEMY2_1_SIZE_X, ENEMY2_1_SIZE_Y =  enemy2_1.get_rect().size[0], \
                                            enemy2_1.get_rect().size[1]
        enemy2_1 = pygame.transform.scale(enemy2_1, (ENEMY2_1_SIZE_X//SRF, ENEMY2_1_SIZE_Y//SRF))
        ENEMY2_1_SIZE_X, ENEMY2_1_SIZE_Y =  enemy2_1.get_rect().size[0], \
                                            enemy2_1.get_rect().size[1]

    elif line[0] == "enemy2_2":
        print("Loading enemy2_2 file: " + line[1])
        enemy2_2 = pygame.image.load(line[1])
        ENEMY2_2_SIZE_X, ENEMY2_2_SIZE_Y =  enemy2_2.get_rect().size[0], \
                                            enemy2_2.get_rect().size[1]
        enemy2_2 = pygame.transform.scale(enemy2_2, (ENEMY2_2_SIZE_X//SRF, ENEMY2_2_SIZE_Y//SRF))
        ENEMY2_2_SIZE_X, ENEMY2_2_SIZE_Y =  enemy2_2.get_rect().size[0], \
                                            enemy2_2.get_rect().size[1]

    elif line[0] == "enemy3_1":
        print("Loading enemy3_1 file: " + line[1])
        enemy3_1 = pygame.image.load(line[1])
        ENEMY3_1_SIZE_X, ENEMY3_1_SIZE_Y =  enemy3_1.get_rect().size[0], \
                                            enemy3_1.get_rect().size[1]
        enemy3_1 = pygame.transform.scale(enemy3_1, (ENEMY3_1_SIZE_X//SRF, ENEMY3_1_SIZE_Y//SRF))
        ENEMY3_1_SIZE_X, ENEMY3_1_SIZE_Y =  enemy3_1.get_rect().size[0], \
                                            enemy3_1.get_rect().size[1]

    elif line[0] == "enemy3_2":
        print("Loading enemy3_2 file: " + line[1])
        enemy3_2 = pygame.image.load(line[1])
        ENEMY3_2_SIZE_X, ENEMY3_2_SIZE_Y =  enemy3_2.get_rect().size[0], \
                                            enemy3_2.get_rect().size[1]
        enemy3_2 = pygame.transform.scale(enemy3_2, (ENEMY3_2_SIZE_X//SRF, ENEMY3_2_SIZE_Y//SRF))
        ENEMY3_2_SIZE_X, ENEMY3_2_SIZE_Y =  enemy3_2.get_rect().size[0], \
                                            enemy3_2.get_rect().size[1]

    elif line[0] == "mothership":
        print("Loading mothership file: " + line[1])
        mothership = pygame.image.load(line[1])
        MOTHER_SIZE_X, MOTHER_SIZE_Y =  mothership.get_rect().size[0], \
                                        mothership.get_rect().size[1]
        mothership = pygame.transform.scale(mothership, (MOTHER_SIZE_X//SRF, MOTHER_SIZE_Y//SRF))
        MOTHER_SIZE_X, MOTHER_SIZE_Y =  mothership.get_rect().size[0], \
                                        mothership.get_rect().size[1]

    elif line[0] == "background":
        print("Loading background file: " + line[1])
        background = pygame.image.load(line[1])

    counter += 1


screen = pygame.display.set_mode((WIDTH,HEIGHT))
background = background.convert()

screen.blit(background, (0,0))

#[Enemies Handler Variables]
enemy1 = [enemy1_1, enemy1_2] # Those variables store enemies with each animation
enemy2 = [enemy2_1, enemy2_2]
enemy3 = [enemy3_1, enemy3_2]
enemiesList = [[0] * enemies_columns for i in range(enemies_rows)] #List for storing enemies
enemiesList_pos = [[0] * enemies_columns for i in range(enemies_rows)] #For storing each enemy position

#[Initial positions sprites]
player_pos_x = WIDTH / 2 - PLAYER_SIZE_X

enemy1_1_pos_x = WIDTH - 30 - ENEMY1_1_SIZE_X
enemy1_1_pos_y = 30

enemy2_1_pos_x = WIDTH - 30 - ENEMY2_1_SIZE_X
enemy2_1_pos_y = enemy1_1_pos_y + ENEMY1_1_SIZE_Y  

enemy3_1_pos_x = WIDTH - 30 - ENEMY3_1_SIZE_X
enemy3_1_pos_y  = enemy2_1_pos_y + ENEMY2_1_SIZE_Y + 5 

def eventHandler():
    '''
    This method takes care of everything related with events.
    '''

    global initialScreen
    global player_pos_x
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
       
        if event.type == pygame.QUIT or keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and initialScreen:
            print("Some key pressed")
            initialScreen = False

    if keys[K_LEFT]: #Player is moving left
        
        if player_pos_x >= 15:
            player_pos_x -= player_movement

    if keys[K_RIGHT]: #Player is moving right
        
        if player_pos_x <= WIDTH - PLAYER_SIZE_X - 15:
            player_pos_x += player_movement

def drawSprite(surface, width, height):
    '''
    Method for drawing sprites.
    '''
    screen.blit(surface,(width,height))

def enemiesHandler():
    global enemy1_1_pos_x, enemy2_1_pos_x, enemy3_1_pos_x, enemy1_1_pos_y, direction

    if enemy1_1_pos_x >= WIDTH - ENEMY1_1_SIZE_X:
        direction = -1
        enemy1_1_pos_y += 30
    elif enemy1_1_pos_x <= 0:
        direction = 1
        enemy1_1_pos_y += 30
    
    enemy1_1_pos_x += enemies_movement * direction
    enemy2_1_pos_x += enemies_movement * direction
    enemy3_1_pos_x += enemies_movement * direction

def ALTenemiesHandler():
    global enemy1_1_pos_x, enemy2_1_pos_x, enemy3_1_pos_x, enemy1_1_pos_y, direction
    
    i = 0
    while i < enemies_rows:
        j = 0
        while j < enemies_columns:
            if enemiesList_pos[i][j][0] >= WIDTH - ENEMY1_1_SIZE_X:
                direction = -1
                enemy1_1_pos_y += 10
            elif enemiesList_pos[i][j][0] <= 0:
                direction = 1
                enemy1_1_pos_y += 10
            j += 1
        i += 1

    enemy1_1_pos_x += enemies_movement * direction
    enemy2_1_pos_x += enemies_movement * direction
    enemy3_1_pos_x += enemies_movement * direction
  
def initializeEnemies():
    '''
    Loads all enemies into enemiesList variable in a matrix form.
    '''
    i = 0
    while i < enemies_rows:
        j = 0
        while j < enemies_columns:
            if i == 0: #Enemy1
                enemiesList[i][j] = enemy1
            elif i == 1: #Enemy2
                enemiesList[i][j] = enemy2
            elif i == 2: #Enemy3
                enemiesList[i][j] = enemy3
            j += 1
        i += 1

    #print(enemiesList)
    offset_y = 0
    i = 0
    for row in enemiesList:
        offset_x = 0
        j = 0
        for enemy in row:
            drawSprite(enemy[0], enemy1_1_pos_x - offset_x, enemy1_1_pos_y + offset_y)
            
            #Store each enemy position in a list.
            enemiesList_pos[i][j] = [enemy1_1_pos_x - offset_x, enemy1_1_pos_y + offset_y]
            offset_x += 40
            j += 1
        offset_y += 40
        i += 1

while True: #main game loop
    if initialScreen: #This code only executes when we're in the initial screen.
        InitialScreen.initialScreenHandler(font_16, font_18, font_35, screen)
        
        if InitialScreen.blink_counter == 50:
            InitialScreen.blink_counter = 0
        else:
            InitialScreen.blink_counter += 1
        
        eventHandler()
    else:
        screen.blit(background,(0,0))
        eventHandler()
        
        drawSprite(player, player_pos_x, HEIGHT - PLAYER_SIZE_Y - 30)
        #drawSprite(enemy1_1, enemy1_1_pos_x, enemy1_1_pos_y)
        #drawSprite(enemy2_1, enemy2_1_pos_x, enemy2_1_pos_y)
        #drawSprite(enemy3_1, enemy3_1_pos_x, enemy3_1_pos_y)
        initializeEnemies()
        ALTenemiesHandler()

    pygame.display.update()
    fpsClock.tick(30)