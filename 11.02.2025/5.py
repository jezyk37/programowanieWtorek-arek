class Widget:
    def __init__(self,label):
        self.label = label

class Button(Widget):

    def __init__(self, label,size):
        super().__init__(label)
        self.size = size

    def handle_click(self):
        return'KLIKNIETO CHOPIE'


b = Button('PRZYCISK', 'DUZY')
print(b.size,b.label)
print(b.handle_click())

w = Widget('my widget')
# w.handle_click() generuje sie error
