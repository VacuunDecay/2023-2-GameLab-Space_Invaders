from pygame import event
from pygame import Vector2
import pygame as pg

from scp.rect import Rect
from scp.tiro import Tiro
from scp.timer import Timer

from PPlay.gameobject import GameObject

class Nave(GameObject):
    def __init__(self, x, y, dif):
        super().__init__()

        # Por favor nao altere x e y diretamente de fora da função. Se isso foce outra linguagem essas variaves estariam protegidas
        self.x = x
        self.y = y

        self.spd = Vector2(1, 0)
        self.dif = dif

        body = Rect(self.x, self.y+5, 45, 20)
        cano = Rect(self.x+20, self.y, 5, 5)

        self.bolets = []
        self.boletTimer = Timer()
        self.boletTimer.start()
        self.boletCoolDown = 1*dif

        self.shape = [body, cano]

    def set_position(self, x, y):
        self.x = x
        self.y = y

        # Temporario; Crie uma classe shape para cuidar de coleções de rects
        self.shape[0].x = self.x
        self.shape[0].y = self.y+5

        self.shape[1].x = self.x+20
        self.shape[1].y = self.y

    def draw(self):
        for s in self.shape:
            s.draw()
        
        for b in self.bolets:
            b.draw()

    def whenKeyUp(self, e):
        pass

    def whenKeyDown(self, e):
        pass
           

    def whenKeyPressed(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_SPACE] and self.boletCoolDown <= self.boletTimer.get_time():
            self.bolets.append(Tiro(self.shape[1].x, self.y, self.dif))
            self.boletTimer.restart()
        if keys[pg.K_LEFT] or keys[pg.K_a]: 
            self.set_position(self.x-self.spd.x, self.y)
        if keys[pg.K_RIGHT] or keys[pg.K_d]: 
                self.set_position(self.x+self.spd.x, self.y)


    def imput(self):
        self.whenKeyPressed()
        """
        for e in event.get():
            if e.type == pg.KEYUP:
                self.whenKeyUp(e)
            if e.type == pg.KEYDOWN:
                self.whenKeyDown(e)
        """

    def update(self):
        self.imput()

        for b in self.bolets:
            b.update()
            if not b.isAlive():
                self.bolets.pop(0)



"""
    for event in pygame.event.get():
        #KeyDown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if sm.game_scene == 'mainMenu':
                    wind.close()
                else:
                    sm.game_scene = 'mainMenu'
"""