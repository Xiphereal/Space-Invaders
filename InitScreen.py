import pygame
import sys


class InitScreen:
    '''
    Initial Space Invaders screen.
    @Author: Alejandro 'Xiph' Lozano
    @Date: February of 2019
    '''

    #[Global Variables]
    HEIGHT = 640
    WIDTH = 480
    SCREEN_X_CENTER = WIDTH / 2
    SCREEN_Y_CENTER = HEIGHT / 2
    

    blink_colors = [(0,255,0), (0,0,0)] #[Green, Black]
    blink_counter = 0

    hi_score = ""

    def __init__(self, score):
        blink_counter = 0
        self.hi_score = str(score)
    
    def initialScreenHandler(self, font_16, font_18, font_35, screen):
        '''
        Draws the initial screen titles into 'screen' parameter.
        '''
        final_color = self.blink_colors[1]
        main_title_space = font_35.render("SPACE", True, (0,255,0))
        main_title_invaders = font_35.render("INVADERS", True, (0,255,0))
        hiscore_title = font_18.render("HI-SCORE: " + self.hi_score, True, (0,255,0))
        
        if self.blink_counter < 25:
            final_color = self.blink_colors[0]
        press_key_title = font_16.render("PRESS ANY KEY TO PLAY", True, final_color)
        
        screen.blit(main_title_space, (150, 160)) 
        screen.blit(main_title_invaders, (100, 210))
        screen.blit(hiscore_title, (120, self.SCREEN_Y_CENTER + 100))
        screen.blit(press_key_title, (70, self.SCREEN_Y_CENTER + 40))
    
