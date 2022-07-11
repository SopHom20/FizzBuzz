import random

class BotTest:
    def __init__(self):
        self.dynamite = 99
        self.where = []
        self.botone = []
        self.bottwo = []
        for i in range(0,100):
            self.where.append(random.randint(0,1000))

        self.currentmove = 0

    def make_move(self, gamestate):
        self.currentmove += 1
        if self.currentmove in self.where:
            if self.dynamite > 0:
                self.dynamite -= 1
                return "D"

        rounds = gamestate['rounds']
        length = len(rounds)
        if length == 0:
            return "S"
        if length == 1:
            return "D"

        self.botone = list(map(lambda x: x['p1'], rounds))
        self.bottwo = list(map(lambda x: x['p2'], rounds))

        lastmove = rounds[length - 1]['p2']
        if self.botone[length - 1] == self.bottwo[length-2]:
            if self.dynamite > 0:
                self.dynamite -= 1
                return "D"
        elif lastmove == rounds[length - 2]['p2']:
            if lastmove == "R":
                return "P"
            elif lastmove == "S":
                return "R"
            elif lastmove == "P":
                return "S"
            elif lastmove == "D":
                return "W"
        else:
            if lastmove == "R":
                return "S"
            elif lastmove == "S":
                return "P"
            elif lastmove == "P":
                return "R"

        return "P"




