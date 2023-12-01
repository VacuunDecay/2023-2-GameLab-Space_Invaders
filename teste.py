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
dificuldade = 0

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
jogar = criar_janela("Space Invaders Game")
mode_scm = criar_janela("img/Game mode")
janela = criar_janela("Space Invaders")


# Imput devices
mouse = Window.get_mouse()
key = Window.get_keyboard()

# Objetos
nave = Player(jogar)
mo = monster_mat(1, 1)
txPonts = Text()


# é o jogo
def jogo():
    global points
    
    nave.set_position(jogar.width/2-nave.width/2, jogar.height - nave.height/2 - 50)
            
    clock = pygame.time.Clock()
    
    while True:
        jogar.set_background_color([0, 0, 0])

        nave.input()

        for t in nave.tiros:
            t.update(jogar, mo)
            t.draw()
            if t.y >= mo.y + mo.height: # se o tiro tiver abixo da matrix ele nao checa colizao
                continue
            if mo.chekColision(t):
                points += 1
                nave.tiros.remove(t)
            elif t.y <= 0:
                nave.tiros.remove(t)

        try:
            fps = 1/jogar.delta_time()
        except:
            fps = 0

        jogar.set_title(str(fps))
        txPonts.set_text(str(points))
        txPonts.draw()
        if mo.y + mo.height > nave.y:
            print("fim de jogo")
            jogar.close()

        mo.draw()
        mo.update(jogar, nave)
        nave.draw()
        jogar.update()
        if(key.key_pressed("ESC")):
            jogar.close()

# Menu seletor de dificuldade
def modes():

    
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
        #print(f'{msDonwP}', end=" ")
        if mouse_mode.is_over_area([x, y_easy], [x+easy.width, y_easy+easy.height]):
            hover.set_position(x, y_easy)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                print("sopa")
                dificuldade = 1
                return dificuldade
        if mouse_mode.is_over_area([x, y_normal], [x+normal.width, y_normal+normal.height]):
            hover.set_position(x, y_normal)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                dificuldade = 2
                jogar.close()
                return dificuldade
        if mouse_mode.is_over_area([x, y_hard], [x+hard.width, y_hard+ hard.height]):
            hover.set_position(x, y_hard)
            hover.draw()
            if msDown(mouse_mode, msDonwSM, msDonwP):
                dificuldade = 3
                mode_scm.close()
                return dificuldade
        mode_scm.update()
        









class Menu1():
    def __init__(self):
        self.mouse = janela.get_mouse()

        self.play = Sprite("img/Play.png")
        self.mode = Sprite("img/Mode.png")
        self.rank = Sprite("img/Rank.png")
        self.quit = Sprite("img/Quit.png")
        self.hover = Sprite("img/Hover.png")

        self.x = janela.width / 2 - self.play.width / 2
        self.y_play = janela.height/2  - 3*self.play.height
        self.y_mode = janela.height/2 - 1.5*self.play.height
        self.y_rank = janela.height/2
        self.y_quit = janela.height/2 + 1.5*self.play.height


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
        if self.mouse.is_over_area([self.x, self.y_play], [self.x+self.play.width, self.y_play+self.play.height]):
            self.hover.set_position(self.x, self.y_play)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                janela.update()
                jogo()
        if self.mouse.is_over_area([self.x, self.y_mode], [self.x+self.mode.width, self.y_mode+self.mode.height]):
            self.hover.set_position(self.x, self.y_mode)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                dificuldade = modes()
                janela.update()
                jogo()
        if self.mouse.is_over_area([self.x, self.y_quit], [self.x+self.quit.width, self.y_quit+self.quit.height]):
            self.hover.set_position(self.x, self.y_quit)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                janela.close()
        if self.mouse.is_over_area([self.x, self.y_rank], [self.x+self.rank.width, self.y_rank+self.rank.height]):
            self.hover.set_position(self.x, self.y_rank)
            self.hover.draw()
            if msDown(self.mouse, msDonwSM, msDonwP):
                pass

    def update(self):
        pass

menu1 = Menu1()

curr_screen = menu1

while True:
    janela.set_background_color([0, 0, 0])


    curr_screen.draw()
    curr_screen.input()
    curr_screen.update()

    

    janela.update()