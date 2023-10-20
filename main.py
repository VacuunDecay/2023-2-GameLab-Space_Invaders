import random as rd

from PPlay.window import *
from PPlay.sprite import *

import time

from scp.menu import Menu
from scp.game import Game
from scp.rect import Rect as R

# Constantes
_height = 455
_width = 802
_TargetFPS = 60
_placarOffset = 50

rd.seed(time.time())

wind = Window(_width, _height)
wind.set_title('Pong')

clock = pygame.time.Clock()
kb = wind.get_keyboard()


menuRect = (_width * 0.5, _height * 0.8)
menuCords = ((_width - menuRect[0]) * 0.5, (_height - menuRect[1]) * 0.5)

menuBox = (menuCords[0], menuCords[1], menuRect[0], menuRect[1])

startM = Menu(menuBox[0], menuBox[1], menuBox[2], menuBox[3], 30)

optionsMenu = Menu(menuBox[0], menuBox[1], menuBox[2], menuBox[3], 30)

class ScineManager:
    def __init__(self):
        self.game_scene = 'mainMenu'
        self.dificulty = 1

    def start_game(self):
        self.game_scene = 'game'

    def game_to_dificult(self):
        self.dificulty = 3
        print(f'{self.dificulty}')
        self.call_halfScreen()

    def game_to_normal(self):
        self.dificulty = 2
        print(f'{self.dificulty}')
        self.call_halfScreen() 

    def game_to_easy(self):
        self.dificulty = 1
        print(f'{self.dificulty}')
        self.call_halfScreen()

    def call_options_menu(self):
        optionsMenu.restart_buttons_timer()
        self.game_scene = 'optionsMenu'

    def call_main_menu(self):
        startM.restart_buttons_timer()
        self.game_sene = 'mainMenu'

    def call_halfScreen(self):
        self.game_scene = 'halfScreen'

    def exit_game(self):
        pygame.quit()
        quit()

sm = ScineManager()

buttonColor = (100, 100, 100)

startM.add_button(sm.start_game, buttonColor, "Start")
startM.add_button(sm.call_options_menu, buttonColor, "Dificuldade")
startM.add_button(None, buttonColor, "Rancking")
startM.add_button(sm.exit_game, buttonColor, "Exit")

optionsMenu.add_button(sm.game_to_dificult, buttonColor, "Dificio")
optionsMenu.add_button(sm.game_to_normal, buttonColor, "Normal")
optionsMenu.add_button(sm.game_to_easy, buttonColor, "Facio")

game = Game(_width, _height, sm.dificulty)

run = True
while run:
    wind.set_background_color([0,12,24])
    clock.tick(_TargetFPS)


    if sm.game_scene == 'mainMenu':
        startM.draw()
        startM.update()


    elif sm.game_scene == 'game':
        game.run()


    elif sm.game_scene == 'optionsMenu':
        optionsMenu.draw()
        optionsMenu.update()

    elif sm.game_scene == 'halfScreen':
        #Do something
        print("on half")
        sm.start_game()




    for event in pygame.event.get():
        #KeyDown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if sm.game_scene == 'mainMenu':
                    wind.close()
                else:
                    sm.game_scene = 'mainMenu'

        if event.type == pygame.QUIT:
            wind.close()
            


    pygame.display.update()