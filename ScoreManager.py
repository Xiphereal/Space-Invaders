import pygame
import os
import sys

class ScoreManager:
    '''
    Manager class for keeping track of player score.
    @Author: Alejandro 'Xiph' Lozano
    @Date: March of 2019
    '''
    score = 0
    
    if not os.path.isfile("hi-score.txt"): #If the file isn't found
        aux = open("hi-score.txt", "w+")
        aux.write("0")
        aux.close()

    hi_score_file = open("hi-score.txt", "r+")

    hi_score = int(hi_score_file.read())
    print(hi_score)

    ENEMY1 = 10
    ENEMY2 = 20
    ENEMY3 = 30
    MOTHERSHIP = 50

    def __init__(self):
        score = 0

    def increase(self, enemyIndex = -1):
        if enemyIndex == -1:
            self.score += self.MOTHERSHIP
        elif enemyIndex % 3 == 0:
            self.score += self.ENEMY1
        elif enemyIndex % 3 == 1:
            self.score += self.ENEMY2
        elif enemyIndex % 3 == 2:
            self.score += self.ENEMY3

        if self.score > self.hi_score:
            self.hi_score = self.score
            self.hi_score_file.close()
            self.hi_score_file = open("hi-score.txt", "w+")
            self.hi_score_file.write(str(self.hi_score))
            self.hi_score_file.close()
            self.hi_score_file = open("hi-score.txt", "r+")
        
        #print(self.score)

    def getScore(self):
        return self.score

    def getHiScore(self):
        return self.hi_score

    def closeFile(self):
        self.hi_score_file.close()
    
    def reset(self):
        self.score = 0

