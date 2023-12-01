import pygame.time as time
import pygame
from scp.timer import Timer
from scp.monstros import *
from scp.text import *
from scp.player import *
from PPlay.window import *
from PPlay.sprite import *

#Game Variables
points = 0
dificuldade = 1.2

msDonwSM = [[0, 0, 0, 0], 
            [1, 2, 2, 2]]
msDonwP = 0

def msDown(mouse, tab, p):
    caso = 0
    global msDonwP
    if mouse.is_button_pressed(1):
        caso = 1
    else:
        caso = 0

    #print(f'({caso}, {p}) |', end=" ")
    #print(f'{tab[caso][p]}', end=" ")
    p = tab[caso][p]
    msDonwP = p
    
    if p == 1:
        return True
    else:
        return False

# cria a tela
def criar_janela(string):
    janela = Window(750, 750)
    janela.set_background_color([0, 0, 0])
    janela.set_title(string)
    return janela

# Telas
mode_scm = criar_janela("img/Game mode")

# Imput devices
mouse = Window.get_mouse()
key = Window.get_keyboard()

# Objetos


class Tela():
    def __init__(self):
        self.screen = criar_janela("Defalt")
        self.dif = 1.3

    def draw(self):
        pass

    def update(self):
        self.screen.update()

    def input(self):
        if(key.key_pressed("ESC")):
            game_scm.close()

class GameOver(Tela):
    def __init__(self):
        self.screen = criar_janela("Game Over")

        self.key = Window.get_keyboard()

        self.points = points
        self.txPoints = Text(points)

    def input(self):
        super().input()

class Game(Tela):
    def __init__(self, dif = 1):
        self.screen = criar_janela("Jogo")

        self.dif = dif

        self.nave = Player(self.screen)
        self.mo = monster_mat(1, 1, dif)
        self.txPonts = Text()
        self.txLives = Text()

        self.txLives.y += 20
        self.nave.set_position(self.screen.width/2-self.nave.width/2, self.screen.height - self.nave.height/2 - 50)

    def input(self):
        super().input()
        self.nave.input()

    def update(self):
        super().update()

        try:
            fps = 1/self.screen.delta_time()
        except:
            fps = 0

        self.screen.set_title(str(fps))
        self.txPonts.set_text(str(self.nave.points))
        self.txLives.set_text(str(self.nave.lives))
        if self.mo.y + self.mo.height > self.nave.y or self.nave.lives <= 0:
            curr_screen = gameOver_scm


        self.mo.update(self.screen, self.nave)
        self.screen.update()

        if self.mo.allDead:
            self.mo = monster_mat(1, 1, self.mo.dif*1.1)
        for t in self.nave.tiros:
            t.update(self.screen, self.mo)
            if t.y >= self.mo.y + self.mo.height: # se o tiro tiver abixo da matrix ele nao checa colizao
                continue
            if self.mo.chekColision(t):
                self.nave.addPoint(self.dif)
                self.nave.tiros.remove(t)
            elif t.y <= 0:
                self.nave.tiros.remove(t)

    def draw(self):
        self.screen.set_background_color([0, 0, 0])

        self.txPonts.draw()
        self.txLives.draw()
        self.mo.draw()
        self.nave.draw()

        for t in self.nave.tiros:
            t.draw()

gameOver_scm = GameOver()
game_scm = Game()
# é o jogo
def jogo(dif = 1.1):
    global curr_screen
    curr_screen = game_scm
    game_scm.dif = dif
    


# Menu seletor de dificuldade
def modes():
    global game_scm
    
    easy = Sprite("img/Easy.png")
    normal = Sprite("img/Normal.png")
    hard = Sprite("img/Hard.png")
    hover = Sprite("img/Hover.png")
    mouse_mode = mode_scm.get_mouse()
    
    x = mode_scm.width / 2 - easy.width / 2
    y_easy = mode_scm.height/2  - 2*easy.height
    y_normal = mode_scm.height/2
    y_hard = mode_scm.height/2 + 2*easy.height
    
    
    easy.set_position(x, y_easy)
    normal.set_position(x, y_normal)
    hard.set_position(x, y_hard)

    while True:
        mode_scm.set_background_color([0, 0, 0])
        easy.draw()
        normal.draw()
        hard.draw()
        if mouse_mode.is_over_area([x, y_easy], [x+easy.width, y_easy+easy.height]):
            hover.set_position(x, y_easy)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                dificuldade = 1
                curr_screen = game_scm
                return dificuldade
        if mouse_mode.is_over_area([x, y_normal], [x+normal.width, y_normal+normal.height]):
            hover.set_position(x, y_normal)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                dificuldade = 2
                curr_screen = game_scm
                return dificuldade
        if mouse_mode.is_over_area([x, y_hard], [x+hard.width, y_hard+ hard.height]):
            hover.set_position(x, y_hard)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                dificuldade = 3
                curr_screen = game_scm
                return dificuldade
        mode_scm.update()
        









class Menu1(Tela):
    def __init__(self):
        super().__init__()
        self.screen = criar_janela("Space Invaders")

        self.mouse = self.screen.get_mouse()

        self.play = Sprite("img/Play.png")
        self.mode = Sprite("img/Mode.png")
        self.rank = Sprite("img/Rank.png")
        self.quit = Sprite("img/Quit.png")
        self.hover = Sprite("img/Hover.png")

        self.x = self.screen.width / 2 - self.play.width / 2
        self.y_play = self.screen.height/2  - 3*self.play.height
        self.y_mode = self.screen.height/2 - 1.5*self.play.height
        self.y_rank = self.screen.height/2
        self.y_quit = self.screen.height/2 + 1.5*self.play.height


        self.quit.set_position(self.x, self.y_quit)
        self.mode.set_position(self.x, self.y_mode)
        self.rank.set_position(self.x, self.y_rank)
        self.play.set_position(self.x, self.y_play)
    
    def draw(self):
        self.play.draw()
        self.mode.draw()
        self.rank.draw()
        self.quit.draw()

    def input(self):
        super().input()
        if self.mouse.is_over_area([self.x, self.y_play], [self.x+self.play.width, self.y_play+self.play.height]):
            self.hover.set_position(self.x, self.y_play)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                self.screen.update()
                jogo(dificuldade)
        if self.mouse.is_over_area([self.x, self.y_mode], [self.x+self.mode.width, self.y_mode+self.mode.height]):
            self.hover.set_position(self.x, self.y_mode)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                dificuldade = modes()
                self.screen.update()
                jogo(dificuldade)
        if self.mouse.is_over_area([self.x, self.y_quit], [self.x+self.quit.width, self.y_quit+self.quit.height]):
            self.hover.set_position(self.x, self.y_quit)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                self.screen.close()
        if self.mouse.is_over_area([self.x, self.y_rank], [self.x+self.rank.width, self.y_rank+self.rank.height]):
            self.hover.set_position(self.x, self.y_rank)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                pass

    def update(self):
        super().update()

menu1 = Menu1()

curr_screen = menu1

while True:
    curr_screen.draw()
    curr_screen.input()
    curr_screen.update()
    print(curr_screen.dif)