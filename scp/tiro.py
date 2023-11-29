from PPlay.sprite import Sprite

from scp.player import Player

class Tiro(Sprite):
    def __init__(self, x, y, isUp: bool = True):
        super().__init__("img/Tiro.png")
        self.x = x
        self.y = y
        self.isUp = isUp
        self.spd = 1
        self.isAlive = True

    def update(self, screen, player: Player):
        if self.isUp:
            self.y-= self.spd
            if self.y < 0:
                self.isAlive = False
        else:
            self.y+= self.spd
            if self.y > screen.height:
                self.isAlive = False

        if self.collided(player):
            player.hit()
