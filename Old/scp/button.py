from PPlay.mouse import Mouse
from pygame.font import Font
import pygame

from enum import Enum

from scp.rect import Rect

class MouseButton(Enum):
    LEFT = 1, 
    RIGHT = 3, 
    MIDLER = 2,



class Button(Rect):
    def __init__(self, x, y, height, width, color = (100, 100, 100), button_action = None, text = "Text"):
        super().__init__(x, y, height, width, color)

        self.start_time = pygame.time.get_ticks()
        self.action_delay = 300

        self.clickCont = 0

        self.hover = False
        self.clicked = False

        self.text = text

        if button_action != None:
            self.action = button_action
        else:
            self.action = self.default_action

        self.trueColor = color
        self.mouse = Mouse()

        self.font = Font(None, 20)

        self.text = self.font.render(text, True, (0, 0, 0))

        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + (self.width / 2), self.y + (self.height / 2))

    def set_text(self, text: str):
        self.text = self.font.render(text, True, (0, 0, 0))
        print('seting')

        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + (self.width / 2), self.y + (self.height / 2))

    def restart_timer(self):
        self.start_time = pygame.time.get_ticks()

    def default_action(self):
            print(f"no function has been assigned to this button")
            print(f'but it have been clicked {self.clickCont}')

    def update(self):
        startpoint = (self.x, self.y)
        endpoint = (self.x + self.width, self.y + self.height)


        if self.mouse.is_over_area(startpoint, endpoint):
            self.hover = True
            current_time = pygame.time.get_ticks()
            
            if current_time - self.start_time < self.action_delay:
                return

            if self.mouse.is_button_pressed(1) and not self.clicked:
                self.clickCont += 1
                self.clicked = True
                self.action()
            elif not self.mouse.is_button_pressed(1):
                self.clicked = False
        else:
            self.hover = False

        self.animate()

    def animate(self):
        if self.hover and self.color[0] >= self.trueColor[0] * 0.5:
            self.change_luminance(0.9)
        elif not self.hover:
            self.color = self.trueColor

    def draw(self):
        super().draw()

        self.sreen.blit(self.text, self.text_rect)

