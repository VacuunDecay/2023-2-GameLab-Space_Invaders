# Imports do PPlay
from PPlay.window import *
from PPlay.sprite import *

# Imports internos
from scp.menu import Menu
from scp.game import Game
'''
Para acessar outros arquivos da pasta scp escreva
from scp.nome_do_arquivo import *
ou
from scp.nome_do_arquivo import nome_da_classe
'''

'''
Mapa do codigo

main
-   menu
--      botao
---         rect
-   game
--      nave
---         rect
---     tiro
---     timer
'''

# Constantes
_height = 455
_width = 802
_TargetFPS = 60
_placarOffset = 50

# Configuração da tela
wind = Window(_width, _height)
wind.set_title('Pong')

clock = pygame.time.Clock()
kb = wind.get_keyboard()

# valores relativos ao tamanho da tela
menuRect = (_width * 0.5, _height * 0.8) # altura e largura respectivamente
menuCords = ((_width - menuRect[0]) * 0.5, (_height - menuRect[1]) * 0.5) # o ponto superior esquerdo

# O ponto superior esquerdo e inferior direito respectivamente, da area onde
# os menus seram confinados
menuBox = (menuCords[0], menuCords[1], menuRect[0], menuRect[1])

# Instanciando menus ( veja o arquivo menu.py para mais detalhes)
startM = Menu(menuBox[0], menuBox[1], menuBox[2], menuBox[3], 30)
optionsMenu = Menu(menuBox[0], menuBox[1], menuBox[2], menuBox[3], 30)

# uma classe para mudar entre cenas
# a variavel game_scene tem o nome da sena a ser executada no momento
# essa classe só muda e guarda essa string com o nome da sena e a dificuldade
# a execução da sena ta sendo feita no rum, usando uma serie de ifs
# um pra cada nome de sena.
# cuidado pra nao digitar os nome errado
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
# Uma instancia da classe assima
sm = ScineManager()

# A cor dos botoes, ta como variavel so pra ficar mais legivel
buttonColor = (100, 100, 100)

# Adicionando botoes os atributos sao respectivamente:
# Uma função que o butao vai executar quando for apertado
# A cor do botao
# Um nome pro botao
# Mas detalhes no arquivo menu.py
startM.add_button(sm.start_game, buttonColor, "Start")
startM.add_button(sm.call_options_menu, buttonColor, "Dificuldade")
startM.add_button(None, buttonColor, "Rancking")
startM.add_button(sm.exit_game, buttonColor, "Exit")

optionsMenu.add_button(sm.game_to_dificult, buttonColor, "Dificio")
optionsMenu.add_button(sm.game_to_normal, buttonColor, "Normal")
optionsMenu.add_button(sm.game_to_easy, buttonColor, "Facio")

# Guarde as coisa do jogo em si aqui
# Jogador, inimigos tiros etc
# Edite o arquivo game.py para isso
game = Game(_width, _height, sm.dificulty)

run = True
while run:
    wind.set_background_color([0,12,24])
    clock.tick(_TargetFPS) # define um fps maximo, isso deixa o jogo mais estavel


    ########################################
    # Ifs para trocar entre cenas
    ## Menu principal
    if sm.game_scene == 'mainMenu':
        startM.draw()
        startM.update()

    ## Jogo ( mais detalhes no arquivo game.py)
    elif sm.game_scene == 'game':
        game.run()

    ## Menu de opsoes
    elif sm.game_scene == 'optionsMenu':
        optionsMenu.draw()
        optionsMenu.update()

    elif sm.game_scene == 'halfScreen':
        #Do something
        print("on half")
        sm.start_game()



    # Imputs ( eu preferi usar o pygame ao inves do pplay por que nao tem um keydonw no pply)
    '''
    key press -> verdadeiro enquanto a tecla for pressionada
    key down -> verdadeiro apenas na primeira vez em que se identifica que a tecla foi presionada
    
    '''
    # Os inputs do jogador estao dentro de jogador
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