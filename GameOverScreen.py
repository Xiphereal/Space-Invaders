import pygame
import sys

class  GameOverScreen:
    '''
    Game Over Space Invaders screen.
    @Author: Alejandro 'Xiph' Lozano
    @Date: March of 2019
    '''

    #[Global Variables]
    HEIGHT = 640
    WIDTH = 480
    SCREEN_X_CENTER = WIDTH / 2
    SCREEN_Y_CENTER = HEIGHT / 2

    blink_colors = [(0,255,0), (0,0,0)] #[Green, Black]
    blink_counter = 0

    hi_score = ""
    #score = ""

    activate_input_counter = 0

    def __init__(self, hi_score):
        blink_counter = 0
        activate_input_counter = 0
        self.hi_score = str(hi_score)

    def gameOverScreenHandler(self, font_16, font_18, font_35, score, screen):
        '''
        Draws the game over screen titles into 'screen' parameter.
        '''
        final_color = self.blink_colors[1]
        main_title_game = font_35.render("GAME", True, (0,255,0))
        main_title_over = font_35.render("OVER", True, (0,255,0))
        hiscore_title = font_18.render("HI-SCORE: " + self.hi_score, True, (0,255,0))
        score_title = font_18.render("SCORE: " + str(score), True, (0,255,0))
        
        if self.blink_counter < 25:
            final_color = self.blink_colors[0]
        press_key_title = font_16.render("PRESS ANY KEY TO PLAY", True, final_color)
        
        screen.blit(main_title_game, (165, 180)) 
        screen.blit(main_title_over, (165, 230))
        screen.blit(hiscore_title, (120, self.SCREEN_Y_CENTER + 80))
        screen.blit(score_title, (174, self.SCREEN_Y_CENTER + 110))
        screen.blit(press_key_title, (70, self.SCREEN_Y_CENTER + 20))
    