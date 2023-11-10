from scp.nave import Nave

class Game:
    
    def __init__(self, w, h, dif):
        self.n = Nave(w/2, h-15-20, dif)

    def run(self):
        self.n.draw()
        self.n.update()




