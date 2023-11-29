from PPlay.sprite import Sprite
from PPlay.window import Window

from scp.timer import Timer

class Player(Sprite):
    def __init__(self, screen: Window, dif = 2):
        super().__init__("img/Spaceship.png")
        self.screen = screen

        self.initPos = (self.screen.width/2-self.width/2, self.screen.height - self.height/2 - 50)

        self.lives = dif*2
        self.hitable = True

        self.cdHit = 5
        self.tmHit = Timer()
        self.tmHit.start()

        self.respawn()

    def respawn(self):
        self.x = self.initPos[0]
        self.y = self.initPos[1]

    def update(self):
        pass
    
    def input(self):
        pass

    def draw(self):

        return super().draw()
    
    def hit(self):
        if self.tmHit.get_time() > self.cdHit:
            self.lives-= 1
            self.tmHit.restart()
            self.respawn()