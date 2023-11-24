import pygame.time as time
import pygame
from scp.timer import Timer
from scp.monstros import *
from scp.text import *

from PPlay.window import *
from PPlay.sprite import *

#Bernardo mendes

#Game Variables
points = 0

# Otimizações 
# - Começar a verificar de baixo pra cima
# - Nao verificar pros tiros fora da caixa de colição da matrix de todos os monstros
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

# é o jogo
def jogo():
    global points
    jogar = criar_janela("Space Invaders Game")
    tecla = Window.get_keyboard()
    nave = Sprite("img/Spaceship.png")
    tiro = Sprite("img/Tiro.png")

    tiros = []

    cooldonw = 0.1
    cooldonwTimer = Timer()
    cooldonwTimer.start()

    velo_nave_y = 300
    velo_nave_x = 300
    velo_tiro = 0
    nave.set_position(jogar.width/2-nave.width/2, jogar.height - nave.height/2 - 50)
            
    clock = pygame.time.Clock()
    while True:
        ##clock.tick(60)
        jogar.set_background_color([0, 0, 0])
        '''
        if(tecla.key_pressed("DOWN") or tecla.key_pressed("s")):
            nave.y += velo_nave_y * jogar.delta_time()
        if(tecla.key_pressed("UP") or tecla.key_pressed("w")):
            nave.y -= velo_nave_y * jogar.delta_time()'''
        if(tecla.key_pressed("RIGHT") or tecla.key_pressed("d")):
            nave.x += velo_nave_x * jogar.delta_time()
        if(tecla.key_pressed("LEFT") or tecla.key_pressed("a")):
            nave.x -= velo_nave_x * jogar.delta_time()
        if(tecla.key_pressed("SPACE")) and cooldonw < cooldonwTimer.get_time():
            tiros.append(Sprite("img/Tiro.png"))
            tiros[-1].set_position(nave.x + nave.width/2 - tiro.width/2, nave.y + nave.height/2 - tiro.height/2)
            velo_tiro= 1000
            cooldonwTimer.restart()

        for t in tiros:
            t.y -= velo_tiro * jogar.delta_time()
            t.draw()
            if t.y >= mo.y + mo.height: # se o tiro tiver abixo da matrix ele nao checa colizao
                continue
            if mo.chekColision(t):
                points += 1
                tiros.remove(t)
            elif t.y <= 0:
                tiros.remove(t)

        try:
            fps = 1/jogar.delta_time()
        except:
            fps = 0

        jogar.set_title(str(fps))
        tx.set_text(str(points))
        tx.draw()
        if mo.y + mo.height > nave.y:
            print("fim de jogo")
            jogar.close()

        mo.draw()
        mo.update(jogar)
        nave.draw()
        jogar.update()
        if(tecla.key_pressed("ESC")):
            jogar.close()

# Menu seletor de dificuldade
def modes():
    jogar = criar_janela("img/Game mode")
    
    easy = Sprite("img/Easy.png")
    normal = Sprite("img/Normal.png")
    hard = Sprite("img/Hard.png")
    hover = Sprite("img/Hover.png")
    mouse_mode = jogar.get_mouse()
    
    x = jogar.width / 2 - easy.width / 2
    y_easy = jogar.height/2  - 2*easy.height
    y_normal = jogar.height/2
    y_hard = jogar.height/2 + 2*easy.height
    
    
    easy.set_position(x, y_easy)
    normal.set_position(x, y_normal)
    hard.set_position(x, y_hard)

    while True:
        jogar.set_background_color([0, 0, 0])
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
                jogar.close()
                return dificuldade
        jogar.update()
        



janela = criar_janela("Space Invaders")
mouse = janela.get_mouse()
dificuldade = 0



play = Sprite("img/Play.png")
mode = Sprite("img/Mode.png")
rank = Sprite("img/Rank.png")
quit = Sprite("img/Quit.png")
hover = Sprite("img/Hover.png")

x = janela.width / 2 - play.width / 2
y_play = janela.height/2  - 3*play.height
y_mode = janela.height/2 - 1.5*play.height
y_rank = janela.height/2
y_quit = janela.height/2 + 1.5*play.height


quit.set_position(x, y_quit)
mode.set_position(x, y_mode)
rank.set_position(x, y_rank)
play.set_position(x, y_play)

mo = monster_mat(1, 1)
tx = Text("Hi")

while True:
    janela.set_background_color([0, 0, 0])
    play.draw()
    mode.draw()
    rank.draw()
    quit.draw()
    if mouse.is_over_area([x, y_play], [x+play.width, y_play+play.height]):
        hover.set_position(x, y_play)
        hover.draw()
        if msDown(mouse, msDonwSM, msDonwP):
            janela.update()
            jogo()
    if mouse.is_over_area([x, y_mode], [x+mode.width, y_mode+mode.height]):
        hover.set_position(x, y_mode)
        hover.draw()
        if msDown(mouse, msDonwSM, msDonwP):
            dificuldade = modes()
            janela.update()
            jogo()
    if mouse.is_over_area([x, y_quit], [x+quit.width, y_quit+quit.height]):
        hover.set_position(x, y_quit)
        hover.draw()
        if msDown(mouse, msDonwSM, msDonwP):
            janela.close()
    if mouse.is_over_area([x, y_rank], [x+rank.width, y_rank+rank.height]):
        hover.set_position(x, y_rank)
        hover.draw()
        if msDown(mouse, msDonwSM, msDonwP):
            pass
    tx.draw()
    janela.update()