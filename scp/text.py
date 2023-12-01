from PPlay.gameobject import GameObject
import pygame

class Text(GameObject):
    def __init__(self, text = ""):
        super().__init__()

        self.text = str(text)

        pygame.font.init()

        self.color = (125, 125, 125)

        self.my_font = pygame.font.SysFont('Comic Sans MS', 25)
        self.text_surface = self.my_font.render(text, False, self.color)
        self.render_text()
        

    def render_text(self):
        lines = self.text.split('\n')
        rendered_lines = [self.my_font.render(line, False, self.color) for line in lines]
        
        max_width = max(line.get_width() for line in rendered_lines)
        total_height = sum(line.get_height() for line in rendered_lines)
        self.text_surface = pygame.Surface((max_width, total_height), pygame.SRCALPHA)

        current_height = 0
        for line in rendered_lines:
            self.text_surface.blit(line, (0, current_height))
            current_height += line.get_height()

    def set_text(self, text):
        self.text = text
        self.text_surface = self.my_font.render(self.text, False, self.color)
    
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.text_surface, (self.x,self.y))

    def __str__(self):
        return self.text