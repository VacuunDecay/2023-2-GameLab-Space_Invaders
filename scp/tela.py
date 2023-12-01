from PPlay.window import Window



def criar_janela(string):
    janela = Window(750, 750)
    janela.set_background_color([0, 0, 0])
    janela.set_title(string)
    return janela


class Tela():
    def __init__(self):
        self.screen = criar_janela("Defalt")
        self.key = self.screen.get_keyboard()
        self.dif = 1.3

    def draw(self):
        self.screen.set_background_color([0, 0, 0])

    def update(self):
        
        self.screen.update()

    def input(self):
        pass