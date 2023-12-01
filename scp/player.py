from PPlay.sprite import Sprite
from PPlay.window import Window

from scp.tiro import Tiro
from scp.timer import Timer

class Player(Sprite):
    def __init__(self, screen: Window, dif = 2):
        super().__init__("img/Spaceship.png")
        self.screen = screen
        self.key = screen.get_keyboard()

        self.initPos = (self.screen.width/2-self.width/2, self.screen.height - self.height/2 - 50)

        self.lives = dif*2
        self.hitable = True

        self.tiros = []
        self.tiro = Tiro(0, 0)
        self.tiro.drawable = False
        
        self.tmHit = Timer()
        self.tmHit.start()
        self.tmHit.set_max_time(2)

        self.spd = 300

        self.cooldonw = Timer()
        self.cooldonw.start()
        self.cooldonw.set_max_time(0.5)

        self.respawn()

    def respawn(self):
        self.x = self.initPos[0]
        self.y = self.initPos[1]

    def update(self):
        pass
    
    def input(self):
        if(self.key.key_pressed("RIGHT") or self.key.key_pressed("d")) and self.x < self.screen.width - self.width:
            self.x += self.spd * self.screen.delta_time()
        if(self.key.key_pressed("LEFT") or self.key.key_pressed("a")) and self.x > 0:
            self.x -= self.spd * self.screen.delta_time()
        if(self.key.key_pressed("SPACE")) and self.cooldonw.ringing():
            self.tiros.append(Tiro(self.x + self.width/2 - self.tiro.width/2, self.y + self.height/2 - self.tiro.height/2))
            self.cooldonw.restart()

    def draw(self):

        return super().draw()
    
    def hit(self):
        if self.tmHit.ringing():
            self.lives-= 1
            self.tmHit.restart()
            self.respawn()