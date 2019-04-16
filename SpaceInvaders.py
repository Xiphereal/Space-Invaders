from pygame.locals import *
import pygame
import sys
import os
import random
import numpy as np
from InitScreen import InitScreen
from GameOverScreen import GameOverScreen
from ScoreManager import ScoreManager
from EnemyBullet import EnemyBullet

'''
This script is a pygame app to recreate Space Invaders.
@Author: Alejandro 'Xiph' Lozano
@Date: February of 2019
'''

#[Global Variables]
HEIGHT = 640
WIDTH = 480
SCREEN_X_CENTER = WIDTH / 2
SCREEN_Y_CENTER = HEIGHT / 2

direction = 1
increase_speed_counter = 1 
any_bullet = False
any_enemy_bullet = False
mothership_spawn = False

initialScreen = True
gameoverScreen = False

#[Pygame Setups]
pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.init()
pygame.display.set_caption("Space Invaders") #Sets the window title
fpsClock = pygame.time.Clock()


#[Pygame Sound]
player_shoot_sound = pygame.mixer.Sound(os.path.join("SFX", "shoot.wav"))
enemy_death_sound = pygame.mixer.Sound(os.path.join("SFX", "invaderkilled.wav"))
player_death_sound = pygame.mixer.Sound(os.path.join("SFX", "player_explosion.wav"))
mothership_sound = pygame.mixer.Sound(os.path.join("SFX", "ufo_lowpitch.wav"))

mothership_channel = pygame.mixer.Channel(5)
 

#[Class instances]
ScoreManager = ScoreManager()
GameOverScreen = GameOverScreen(ScoreManager.getHiScore())
InitialScreen = InitScreen(ScoreManager.getHiScore())

#[Gameplay variables]
player_movement = 5
player_lives = 3
shoot_speed = 22

enemies_rows = 6
enemies_columns = 7
enemies_movement = 1
enemies_speed_increase = 1
enemies_bullet_speed = 2 #Should be 10
enemies_limit = HEIGHT - 70

mothership_movement = 7


#[Fonts initialitation]
font_16 = pygame.font.Font("PressStart2P.ttf", 16)
font_18 = pygame.font.Font("PressStart2P.ttf", 18)
font_35 = pygame.font.Font("PressStart2P.ttf", 35)


#Stores "spriteID.txt" content in a list. Then, evaluates the ID for loading sprites.
spriteID = open("spritesID.txt").readlines()

counter = 0
while counter < len(spriteID):
    line = spriteID[counter].split()
    SRF = 4 #Sprite Redimension Factor: How much will the sprites be downscaled.

    if line[0] == "player":
        print("Loading player file: " + line[1])
        player = pygame.image.load(line[1])
        PLAYER_SIZE_X, PLAYER_SIZE_Y = player.get_rect().size[0], \
                                        player.get_rect().size[1]
        player = pygame.transform.scale(player, (PLAYER_SIZE_X//3, PLAYER_SIZE_Y//3))
        PLAYER_SIZE_X, PLAYER_SIZE_Y = player.get_rect().size[0], \
                                        player.get_rect().size[1]

    elif line[0] == "enemy1_1":
        print("Loading enemy1_1 file: " + line[1])
        enemy1_1 = pygame.image.load(line[1])
        ENEMY1_1_SIZE_X, ENEMY1_1_SIZE_Y =  enemy1_1.get_rect().size[0], \
                                            enemy1_1.get_rect().size[1]
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

    elif line[0] == "bullet":
        print("Loading bullet file: " + line[1])
        bullet = pygame.image.load(line[1])
        BULLET_SIZE_X, BULLET_SIZE_Y = bullet.get_rect().size[0], \
                                       bullet.get_rect().size[1]
        bullet = pygame.transform.scale(bullet, (BULLET_SIZE_X * 2, BULLET_SIZE_Y * 2))
        BULLET_SIZE_X, BULLET_SIZE_Y = bullet.get_rect().size[0], \
                                       bullet.get_rect().size[1]
    elif line[0] == "enemy_bullet":
        print("Loading bullet file: " + line[1])
        enemy_bullet = pygame.image.load(line[1])
        ENEMY_BULLET_SIZE_X, ENEMY_BULLET_SIZE_Y = enemy_bullet.get_rect().size[0], \
                                       enemy_bullet.get_rect().size[1]
        enemy_bullet = pygame.transform.scale(enemy_bullet, (ENEMY_BULLET_SIZE_X * 2, ENEMY_BULLET_SIZE_Y * 2))
        ENEMY_BULLET_SIZE_X, ENEMY_BULLET_SIZE_Y = enemy_bullet.get_rect().size[0], \
                                       enemy_bullet.get_rect().size[1]

    elif line[0] == "background":
        print("Loading background file: " + line[1])
        background = pygame.image.load(line[1])

    counter += 1


screen = pygame.display.set_mode((WIDTH,HEIGHT)) #Sets the screen dimensions and store the object.
background = background.convert()

#[Enemies Handler Variables]
enemy1 = [enemy1_1, enemy1_2] # Those variables store enemies with each animation.
enemy2 = [enemy2_1, enemy2_2]
enemy3 = [enemy3_1, enemy3_2]
enemiesList = [[0] * enemies_columns for i in range(enemies_rows)] #Matrix for storing enemies.
enemiesList_pos = [[0] * enemies_columns for i in range(enemies_rows)] #For storing each enemy position.
enemiesList_active = np.zeros((enemies_rows, enemies_columns), dtype = bool) #For storing, ehh... yeah, another list.
enemiesList_bullets = np.zeros((enemies_rows, enemies_columns), dtype = EnemyBullet) #U think we already had enought list?.

#[Initial sprites position]
player_pos_x = WIDTH / 2 - PLAYER_SIZE_X
player_pos_y = HEIGHT - PLAYER_SIZE_Y - 30

enemy1_1_pos_x = WIDTH - 30 - ENEMY1_1_SIZE_X
enemy1_1_pos_y = 50

enemy2_1_pos_x = WIDTH - 30 - ENEMY2_1_SIZE_X
enemy2_1_pos_y = enemy1_1_pos_y + ENEMY1_1_SIZE_Y

enemy3_1_pos_x = WIDTH - 30 - ENEMY3_1_SIZE_X
enemy3_1_pos_y = enemy2_1_pos_y + ENEMY2_1_SIZE_Y + 5

mothership_pos_x = 0 - MOTHER_SIZE_X
mothership_pos_y = 30

bullet_pos_x = player_pos_x + PLAYER_SIZE_X // 2 - 6
bullet_pos_y = player_pos_y + 12

#enemy_bullet_pos_x = -1000 
#enemy_bullet_pos_y = -1000

#Loads all enemies into enemiesList variable, in a matrix form.
i = 0
while i < enemies_rows:
    j = 0
    while j < enemies_columns:
       
        if i % 3 == 0: #Enemy1
            enemiesList[i][j] = enemy1
        elif i % 3 == 1: #Enemy2
            enemiesList[i][j] = enemy2
        elif i % 3 == 2: #Enemy3
            enemiesList[i][j] = enemy3
        enemiesList_active[i,j] = True

        j += 1
    i += 1
#print(enemiesList)

def eventHandler():
    '''
    This method takes care of everything related with inputs.
    '''
    global initialScreen, gameoverScreen, player_pos_x, any_bullet

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT or keys[K_ESCAPE]:
            ScoreManager.closeFile()
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and initialScreen:
            #print("Some key pressed")
            initialScreen = False
        
        if event.type == pygame.KEYDOWN and gameoverScreen:
            #print("Some key pressed")
            gameoverScreen = False
            ScoreManager.reset()


    if keys[K_LEFT]: #Player is moving left

        if player_pos_x >= 15:
            player_pos_x -= player_movement

    elif keys[K_RIGHT]: #Player is moving right

        if player_pos_x <= WIDTH - PLAYER_SIZE_X - 15:
            player_pos_x += player_movement

    if keys[K_SPACE]: #Player fires!
        if not any_bullet:
            player_shoot_sound.set_volume(0.6)
            player_shoot_sound.play()
            bullet_pos_x = player_pos_x + PLAYER_SIZE_X // 2 - 6
            bullet_pos_y = player_pos_y + 12
            drawSprite(bullet, bullet_pos_x, bullet_pos_y)
            any_bullet = True

def drawSprite(surface, width, height):
    '''
    Method for drawing sprites.
    '''
    screen.blit(surface,(width,height))

def uiManager():
    '''
    Method for all the stuff related with UI
    '''
    global screen, font_16, font_18, font_35, player_lives
    
    player_lives_number = font_16.render(str(player_lives), True, (255,255,255))
    score_title = font_16.render("SCORE", True, (255,255,255))
    score_number = font_16.render(str(ScoreManager.getScore()), True, (255,255,255))
    hi_score_title = font_16.render("HI-SCORE", True, (255,255,255))
    hi_score_number = font_16.render(str(ScoreManager.getHiScore()), True, (255,255,255))

    #Upper UI
    screen.blit(score_title, (8, 10))
    screen.blit(hi_score_title, (130, 10))

    screen.blit(score_number, (20, 30))
    screen.blit(hi_score_number, (170, 30))
    
    #Lower UI
    pygame.draw.line(screen, (0,255,0), (0, HEIGHT - 28), (WIDTH, HEIGHT - 28), 2)

    resized_player = pygame.transform.scale(player, (PLAYER_SIZE_X // 2, PLAYER_SIZE_Y // 2))

    if player_lives == 3:
        drawSprite(resized_player, 43, HEIGHT - 30)
        drawSprite(resized_player, 72, HEIGHT - 30)
    elif player_lives == 2:
        drawSprite(resized_player, 43, HEIGHT - 30)
    
    screen.blit(player_lives_number, (14, HEIGHT - 22))

def isColliding(pos_x, pos_y, width, height, bullet_x, bullet_y):
    '''
    Checks if the sprite passed is colliding with the bullet. 
    '''
    #global bullet_pos_x, bullet_pos_y
    #print(bullet_x, " ", bullet_x)
    return (bullet_x >= pos_x and bullet_x <= pos_x + width) and \
            (bullet_y >= pos_y and bullet_y <= pos_y + height) 

def frontEnemy(target_i,target_j):
    '''
    Iterates through the column looking for the lowest active enemy.
    Is the lower enemy the actual enemy? Then open fire!
    '''
    lower_enemy = -1

    i = 0
    while i < enemies_rows:
        lower_enemy = i if enemiesList_active[i][target_j] == True else lower_enemy
        i += 1

    return target_i == lower_enemy 


def enemiesHandler():
    '''
    Method for all the related stuff going on with enemies.
    '''
    global enemy1_1_pos_x, enemy2_1_pos_x, enemy3_1_pos_x, enemy1_1_pos_y, direction
    global increase_speed_counter, enemies_movement
    global any_bullet

    enemies_left = False
    row_already_lowered = False

    i = 0
    while i < enemies_rows:
        j = 0
        while j < enemies_columns:

            #Check if the actual enemy is colliding with the bullet. 
            if isColliding(enemiesList_pos[i][j][0], enemiesList_pos[i][j][1], \
                            ENEMY1_1_SIZE_X, ENEMY1_1_SIZE_Y, bullet_pos_x, bullet_pos_y) \
                    and enemiesList_active[i,j] == True:
                #print("Colliding with: ", enemiesList[i][j])
                enemy_death_sound.set_volume(0.8)
                enemy_death_sound.play()
                any_bullet = False #Deletes bullet
                enemiesList_active[i,j] = False #""deletes"" the enemy.
                ScoreManager.increase(i)
            
            #Check if the enemy is able to shoot.
            if frontEnemy(i,j):

                if enemiesList_bullets[i,j] == 0:
                    enemiesList_bullets[i,j] = EnemyBullet()

                enemyShootHandler(enemiesList_bullets[i,j], \
                                    enemiesList_pos[i][j][0], enemiesList_pos[i][j][1])

            #If the enemy is killed (either it's not front enemy anymore), bullet keeps traversing the screen.
            elif enemiesList_bullets[i,j] != 0 and enemiesList_bullets[i,j].getSpawn(): 
                
                    enemyShootHandler(enemiesList_bullets[i,j], \
                                        enemiesList_pos[i][j][0], enemiesList_pos[i][j][1])
            
            #GameOver state.
            if enemiesList_pos[i][j][1] >= enemies_limit:
                initGame()
                gameoverScreen = True

            #Update direction when side limit is reached.
            if enemiesList_pos[i][j][0] >= WIDTH - ENEMY1_1_SIZE_X:
                direction = -1

                if not row_already_lowered:
                    enemy1_1_pos_y += 30
                    row_already_lowered = True

            elif enemiesList_pos[i][j][0] <= 0:
                direction = 1

                if not row_already_lowered:
                    enemy1_1_pos_y += 30
                    row_already_lowered = True
            
            #Check if there's any enemy left
            if enemiesList_active[i,j] == True:
                enemies_left = True

            j += 1
        i += 1
    
    #Win state if there's no enemy left
    if not enemies_left:
        #pauseFor()
        initGame()

    #After a while, increases the enemies movement.
    if increase_speed_counter % 500 == 0:
        enemies_movement += enemies_speed_increase
    
    increase_speed_counter += 1

    #print("Enemies movement: ", enemies_movement)
    #print("Increased speed counter: ", increase_speed_counter)
    enemy1_1_pos_x += enemies_movement * direction
    enemy2_1_pos_x += enemies_movement * direction
    enemy3_1_pos_x += enemies_movement * direction

def mothershipHandler():
    global mothership_pos_x, mothership_pos_y, mothership_spawn
    global any_bullet
    
    spawn_proc = random.randint(1,1000)
    #print(spawn_proc)
    if spawn_proc % 500 == 0:
        mothership_spawn = True
        if not mothership_channel.get_busy():
            mothership_channel.play(mothership_sound)

    if isColliding(mothership_pos_x, mothership_pos_y, MOTHER_SIZE_X, MOTHER_SIZE_Y, \
                    bullet_pos_x, bullet_pos_y):
        mothership_sound.stop()
        enemy_death_sound.play()
        any_bullet = False #Deletes bullet.
        mothership_spawn = False #Deletes mothership.
        ScoreManager.increase()

    if mothership_pos_x >= 0 - MOTHER_SIZE_X  \
            and mothership_pos_x <= WIDTH \
            and mothership_spawn:
        
        drawSprite(mothership, mothership_pos_x, mothership_pos_y)
        mothership_pos_x += mothership_movement
    else:
        mothership_pos_x = 0 - MOTHER_SIZE_X
        mothership_spawn = False

def initGame():
    global enemiesList, enemiesList_pos, enemiesList_active, enemiesList_bullets
    global player_pos_x, player_pos_y, player_lives, any_bullet
    global enemy1_1_pos_x, enemy1_1_pos_y, enemy2_1_pos_x, enemy2_1_pos_y, enemy3_1_pos_x, enemy3_1_pos_y
    global enemies_movement, mothership_pos_y, MOTHER_SIZE_Y

    #Reinitialize meaninful position variables
    player_pos_x = WIDTH / 2 - PLAYER_SIZE_X
    player_pos_y = HEIGHT - PLAYER_SIZE_Y - 35

    enemy1_1_pos_x = WIDTH - 180 - ENEMY1_1_SIZE_X
    enemy1_1_pos_y = mothership_pos_y + MOTHER_SIZE_Y

    enemy2_1_pos_x = WIDTH - 30 - ENEMY2_1_SIZE_X
    enemy2_1_pos_y = enemy1_1_pos_y + ENEMY1_1_SIZE_Y

    enemy3_1_pos_x = WIDTH - 30 - ENEMY3_1_SIZE_X
    enemy3_1_pos_y = enemy2_1_pos_y + ENEMY2_1_SIZE_Y + 5

    mothership_pos_x = 0 - MOTHER_SIZE_X
    mothership_pos_y = 30

    #Update other variables
    any_bullet = False
    enemies_movement = 1
    

    #Loads all enemies into enemiesList variable, in a matrix form.
    i = 0
    while i < enemies_rows:
        j = 0
        while j < enemies_columns:
        
            if i % 3 == 0: #Enemy1
                enemiesList[i][j] = enemy1
            elif i % 3 == 1: #Enemy2
                enemiesList[i][j] = enemy2
            elif i % 3 == 2: #Enemy3
                enemiesList[i][j] = enemy3
            enemiesList_active[i,j] = True

            #Destroy all enemies bullets instances
            if enemiesList_bullets[i,j] != 0:
                enemiesList_bullets[i,j].setSpawn(False)

            j += 1
        i += 1

    
def shootHandler():
    global bullet_pos_x, bullet_pos_y, any_bullet
    #print(any_bullet)
    #print("Bullet before if: ", bullet_pos_y)
    if bullet_pos_y > 0 and any_bullet:
        #print(bullet_pos_y)
        bullet_pos_y -= shoot_speed
        drawSprite(bullet, bullet_pos_x, bullet_pos_y)
    else:
        bullet_pos_x = player_pos_x + PLAYER_SIZE_X // 2 - 6
        bullet_pos_y = player_pos_y + 12
        any_bullet = False


def enemyShootHandler(bullet_instance, pos_x, pos_y):
    global initialScreen, gameoverScreen, player_lives, any_bullet

    enemy_shoot_proc = random.randint(1,1000)
    #print(enemy_shoot_proc)
    if enemy_shoot_proc % 250 == 0:
        #print("Shooting!")
        bullet_instance.setSpawn(True)
        
    if bullet_instance.getPosY() < HEIGHT - ENEMY_BULLET_SIZE_Y \
            and bullet_instance.getSpawn():
        #print("Updating enemy bullet position")
        bullet_instance.setPosY(bullet_instance.getPosY() + enemies_bullet_speed)
        #print(bullet_instance.getPosY())
        drawSprite(enemy_bullet, bullet_instance.getPosX(), bullet_instance.getPosY())
    else:
        bullet_instance.setPosX(pos_x + ENEMY1_1_SIZE_X // 2)
        bullet_instance.setPosY(pos_y + ENEMY1_1_SIZE_Y)
        #Destroy bullet
        bullet_instance.setSpawn(False)

    #Check wheter the bullet hits the player
    if isColliding(player_pos_x, player_pos_y, PLAYER_SIZE_X, PLAYER_SIZE_Y, \
                    bullet_instance.getPosX(), bullet_instance.getPosY()):
        print("Player hit!")
        player_death_sound.play()
        player_lives -= 1
        bullet_instance.setSpawn(False)
        pauseFor(2)
        
        if player_lives == 0: #Player is dead: game overstate
            gameoverScreen = True

    #Check if bullets collide with each other
    if isColliding(bullet_pos_x, bullet_pos_y, BULLET_SIZE_X + 5, BULLET_SIZE_Y + 5, \
                        bullet_instance.getPosX(), bullet_instance.getPosY()):
        bullet_instance.setSpawn(False)
        any_bullet = False



def pauseFor(time = 1):
    '''
    Method for stopping the game loop for a certain amount of time.
    At 30 fps, 30 increments per seconds.
    '''
    time *= 30
    counter = 0
    while counter < time:
        #screen.blit(background,(0,0))
        pygame.display.update()
        fpsClock.tick(30)
        counter += 1
    

def drawEnemies():
    '''
    Draws all enemies inside enemiesList variable.
    '''  
    offset_y = 0
    i = 0
    for row in enemiesList:
        offset_x = 0
        j = 0
        for enemy in row:
            
            if enemiesList_active[i][j] == True:
                drawSprite(enemy[0], enemy1_1_pos_x - offset_x, enemy1_1_pos_y + offset_y)
                #Store each enemy position in a list.
                enemiesList_pos[i][j] = [enemy1_1_pos_x - offset_x, enemy1_1_pos_y + offset_y]

            offset_x += 40
            j += 1
        offset_y += 40
        i += 1

while True: 
    '''
    Main game loop.
    '''

    if initialScreen: #This code only executes when we're in the initial screen.
        screen.blit(background, (0,0))
        InitialScreen.initialScreenHandler(font_16, font_18, font_35, screen)
        initGame()
        player_lives = 3

        #InitialScreen.blink_counter = 0 if InitialScreen.blink_counter == 50 else InitialScreen.blink_counter + 1
        if InitialScreen.blink_counter == 50:
            InitialScreen.blink_counter = 0
        else:
            InitialScreen.blink_counter += 1

        eventHandler()

    elif gameoverScreen: #game over code block
        screen.blit(background, (0,0))
        GameOverScreen.gameOverScreenHandler(font_16, font_18, font_35, ScoreManager.getScore(), screen)
        initGame()
        
        player_lives = 3

        if GameOverScreen.blink_counter == 50:
            GameOverScreen.blink_counter = 0
        else:
            GameOverScreen.blink_counter += 1

        if GameOverScreen.activate_input_counter > 100:
            eventHandler()
        else:
            GameOverScreen.activate_input_counter += 1

    else:
        screen.blit(background,(0,0))
        eventHandler()
        uiManager()

        drawSprite(player, player_pos_x, player_pos_y)
        #drawSprite(enemy1_1, enemy1_1_pos_x, enemy1_1_pos_y)
        #drawSprite(enemy2_1, enemy2_1_pos_x, enemy2_1_pos_y)
        #drawSprite(enemy3_1, enemy3_1_pos_x, enemy3_1_pos_y)
        drawEnemies()
        enemiesHandler()
        mothershipHandler()
        shootHandler()
        

    pygame.display.update()
    fpsClock.tick(30)
