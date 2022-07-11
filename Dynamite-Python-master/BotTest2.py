import random

class BotTest2:
    def __init__(self):
        self.dynamite = 100

    def make_move(self, gamestate):

        options = ['R', 'P', 'S', 'D']
        choice = random.choice(options)

        if 'D' in choice:
            self.dynamite -= 1
            if self.dynamite < 0:
                choice = 'P'

        return choice
