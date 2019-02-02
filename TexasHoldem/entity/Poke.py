class Poke:
    color = ''
    number = ''

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def printpoke(self):
        print(self.color + '|' + self.number)