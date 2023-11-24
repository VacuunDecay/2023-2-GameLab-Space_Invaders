from PPlay.gameobject import GameObject
from PPlay.sprite import Sprite
from PPlay.window import Window
import pygame
from enum import Enum


TOP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class monster_mat(GameObject):
    #Obs L = Colunas e C = Linhas
    #Fiz tudo trocado e agora ja é tarde de mais pra refatorar
    def __init__(self, L, C):
        super().__init__()
        if L < 6:
            L = 6

        if C < 4:
            C = 4
        self.C = C
            
        self.L = L
        self.mat = [[None]*C for _ in range(L)]
        moster = Sprite("img\Spaceship.png")
        self.offsetX = moster.height*1.5
        self.offsetY = moster.width*1.5

        self.moveLeft = False
        self.screen = pygame.display.get_surface()

        self.spdX = 100
        self.spdY = 10

        self.borders = [L, C, L, C] # number of ships ant the most Top, right, donw, and left respectively


        self.width = L*self.offsetX+self.x - (self.offsetX/3)
        self.height = C*self.offsetY+self.y - (self.offsetY/3)

        for l in range(self.L):
            for c in range(self.C):
                self.mat[l][c] = Sprite("img\Spaceship.png")
                self.mat[l][c].set_position(l*self.offsetX+self.x, c*self.offsetY+self.y)
            #print(self.mat[l])

    def update(self, wind: Window):
        delta = wind.delta_time()

        if self.moveLeft: 
            if self.x < 0:
                self.y += self.spdY
                self.moveLeft = False
            else:
                self.x -= self.spdX * delta
        else:
            if self.x+self.width > wind.width :
                self.y += self.spdY
                self.moveLeft = True
            else:
                self.x += self.spdX * delta

        for l in range(self.L):
            for c in range(self.C):
                self.mat[l][c].set_position(l*self.offsetX+self.x, c*self.offsetY+self.y)

    def calcDimations(self):
        self.width = self.L*self.offsetX+self.x - (self.offsetX/3)
        self.height = self.C*self.offsetY+self.y - (self.offsetY/3)

        for l in range(self.L):
            for c in range(self.C):
                pass

    def draw(self):
        for l in range(self.L):
            for c in range(self.C):
                self.mat[l][c].draw()

    def remove(self, line, col):
        hit = self.mat[line][col]
        hit.drawable = False
        hit.height = 0
        hit.width = 0


    def chekColision(self, tiro: Sprite):
        for c in reversed(range(self.C)): # Começa pela linha mais a baixo e vai subindo
            for l in range(self.L):
                if self.mat[l][c].collided(tiro) and self.mat[l][c].drawable:
                    self.remove(l, c)
                    self.calcDimations()
                    return True
        return False


