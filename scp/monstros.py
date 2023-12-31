from PPlay.gameobject import GameObject
from PPlay.sprite import Sprite
from PPlay.window import Window
import pygame
from enum import Enum
import random as rd
from scp.tiro import *
from scp.timer import *
from scp.rect import *


class monster_mat(GameObject):
    #Obs L = Colunas e C = Linhas
    #Fiz tudo trocado e agora ja é tarde de mais pra refatorar
    def __init__(self, L, C, dificuldade = 1):
        super().__init__()
        if L < 6:
            L = 6

        if C < 4:
            C = 4
        self.C = C

        if dificuldade <= 0:
            dificuldade = 1    
        self.dif = dificuldade

        self.deadCont = 0

        self.L = L
        self.mat = [[None]*L for _ in range(C)]

        self.mosterSpt = "img/Spaceship.png"
        moster = Sprite(self.mosterSpt)

        self.moster = moster
        self.offsetX = moster.height*1.5
        self.offsetY = moster.width*1.5

        self.moveLeft = False
        self.screen = pygame.display.get_surface()

        self.spdX = 100*self.dif
        self.spdY = 10 *self.dif

        self.allDead = False

        self.width = L*self.offsetX+self.x - (self.offsetX/3)
        self.height = C*self.offsetY+self.y - (self.offsetY/3)

        self.tiros = []
        self.tiroClock = Timer()
        self.cdTiro = 1/self.dif

        self.tiroClock.start()


        for l in range(self.L):
            for c in range(self.C):
                self.mat[c][l] = Sprite(self.mosterSpt)
                self.mat[c][l].set_position(l*self.offsetX+self.x, c*self.offsetY+self.y)
            #print(self.mat[l])


    def chengeDirection(self, wind, delta):
        for l in range(self.L):
            for c in range(self.C):
                if self.mat[c][l].drawable:
                    if self.mat[c][l].x < 0:
                        if self.moveLeft:
                            self.y += self.spdY
                            self.moveLeft = False
                    elif self.mat[c][l].x+self.mat[c][l].width > wind.width:
                        if not self.moveLeft:
                            self.y += self.spdY
                            self.moveLeft = True
        if delta > 1:
            delta = 1

        if self.moveLeft:
            self.x -= self.spdX * delta
        else:
            self.x += self.spdX * delta

    def update(self, wind: Window, player):
        delta = wind.delta_time()

        if self.tiroClock.get_time() > self.cdTiro:
            self.fire()
            self.tiroClock.start()

        for t in self.tiros:
            if t.isAlive:
                t.update(wind, player)

        self.chengeDirection(wind, delta)

        for l in range(self.L):
            for c in range(self.C):
                self.mat[c][l].set_position(l*self.offsetX+self.x, c*self.offsetY+self.y)


    def draw(self):
        #print(f'{self.x}, {self.y}')
        for t in self.tiros:
            if t.isAlive:
                t.draw()

        # Rect(self.x, self.y, self.width, self.height).draw()

        for l in range(self.L):
            for c in range(self.C):
                self.mat[c][l].draw()

    def setC(self, val):
        self.C = val
        self.width = self.L*self.offsetX+self.x - (self.offsetX/3)
        print(self.C)

    def remove(self, line, col):
        hit = self.mat[col][line]
        hit.drawable = False
        hit.height = 0
        hit.width = 0
        self.deadCont += 1
        if self.deadCont >= self.C * self.L:
            self.allDead = True


    '''def collided(self, tiro: Sprite):
        for c in reversed(range(self.C)): # Começa pela linha mais a baixo e vai subindo
            for l in range(self.L):
                if self.mat[c][l].collided(tiro) and self.mat[c][l].drawable:
                    self.remove(l, c)
                    return True
        return False
    '''
    def hit(self):
        pass

    def chekColision(self, tiro: Sprite):
        for c in reversed(range(self.C)): # Começa pela linha mais a baixo e vai subindo
            for l in range(self.L):
                if self.mat[c][l].collided(tiro) and self.mat[c][l].drawable:
                    self.remove(l, c)
                    return True
        return False

    def fire(self):
        shooter = self.mat[rd.randint(0, self.C-1)][rd.randint(0, self.L-1)]

        cont = 0

        while not shooter.drawable and cont < 24:
            shooter = self.mat[rd.randint(0, self.C-1)][rd.randint(0, self.L-1)]
            cont+= 1

        tiro = Tiro(shooter.x+(self.moster.width/2), shooter.y+(self.moster.height/2), False)

        if cont < 24:
            self.tiros.append(tiro)
            


