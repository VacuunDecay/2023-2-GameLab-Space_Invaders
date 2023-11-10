from scp.button import Button

"""
O menu guarda botoes
voce adiciona botoes com o metodo(função) add_bottao
"""

class Menu:
    def __init__(self, x, y, width, height, buttonH = None):
        self.buttons = []
        self.buttonCont = 0

        self.x, self.y, self.width, self.height = x, y, width, height


        if buttonH == None:
            buttonH = self.height
        self.buttonH = buttonH

        self.gap = 0.2 # the gap between buttons

    def draw(self):
        for b in self.buttons:
            b.draw()

    def update(self):
        for b in self.buttons:
            b.update()

    def set_button_text(self, button, text):
        try:
            self.buttons[button].set_text(text)
        except:
            print(f'there is no button {button}')

    def restart_buttons_timer(self):
        for b in self.buttons:
            b.restart_timer()

    def add_button(self, button_action, color, text = "Text"):
        lastButton = self.buttonCont -1
        self.buttonCont += 1

        y_offset = self.height/self.buttonCont
        
        width = self.width
        height = y_offset * (1-self.gap)

        curButton = 0

        if lastButton < 0:
            self.buttons.append(Button(self.x, self.y, width, self.buttonH, color, button_action, text))
            return

        if self.buttons[lastButton].y + self.buttons[lastButton].height > self.y + self.height:
            for b in self.buttons:
                b.y = self.y + (y_offset * curButton)
                b.height = height      

                curButton += 1
            self.buttons.append(Button(self.x, self.y + (y_offset * curButton) , width, height, color, button_action, text))
        else:
            self.buttons.append(Button(self.x, self.y + (self.buttonH * len(self.buttons) / (1-self.gap)), width, self.buttonH, color, button_action, text))
