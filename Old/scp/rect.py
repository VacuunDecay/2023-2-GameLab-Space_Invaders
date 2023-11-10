from PPlay.gameobject import GameObject

from pygame import draw as pyDraw
from pygame import display

class Rect(GameObject):
    def __init__(self, x, y, width, height, color = (100, 100, 100)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.sreen = display.get_surface()
        self.color = color

    def draw(self):
        self.static_draw(self.x, self.y, self.width, self.height, self.color)

    @staticmethod
    def static_draw(x, y, width, height, color = (100, 100, 100)):
        sreen = display.get_surface()
        pyDraw.rect(sreen, color, (x, y, width, height))

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    

    def change_luminance(self, factor):
        oldColor = self.color
        
        r = self.color[0] * factor
        g = self.color[1] * factor
        b = self.color[2] * factor

        self.color = (r, g, b)

        return oldColor