from PPlay.gameobject import GameObject
import pygame

class Text(GameObject):
    def __init__(self, text = ""):
        super().__init__()

        text = str(text)

        pygame.font.init() # you have to call this at the start,
        #if you want to use this module.
        self.color = (125, 125, 125)

        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render(text, False, self.color)

    def set_text(self, text):
        self.text_surface = self.my_font.render(text, False, self.color)
    
    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.text_surface, (self.x,self.y))