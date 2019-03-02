import pygame

class EnemyBullet:
    '''
    Class for enemies instanciate bullets.
    '''
    pos_x = 10 
    pos_y = 10
    spawn = False

    def __init__(self):
        pass

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def getSpawn(self):
        return self.spawn

    def setPosX(self, new_value):
        self.pos_x = new_value
    
    def setPosY(self, new_value):
        self.pos_y = new_value

    def setSpawn(self, new_value):
        self.spawn = new_value
