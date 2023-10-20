from PPlay.sprite import Sprite
from PPlay.gameobject import GameObject

from pygame import Vector2
from pygame import time as time
from pygame import display

from scp.rect import Rect
from scp.timer import Timer

class Tiro(Rect):
    
    def __init__(self, x, y, dif):
        super().__init__(x, y, 5, 20)


        self.screen = display.get_surface()
        self.clock = Timer()
        self.clock.start()

        self.speed = Vector2(0, -2/(dif*2))
        self.lifeTime = 10

    
    def update(self):
        self.y += self.speed.y
        self.x += self.speed.x    


    def isAlive(self) -> bool:
        return self.clock.get_time() < self.lifeTime

    def draw(self):
        super().draw()