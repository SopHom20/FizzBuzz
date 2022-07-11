import random


class BotTest3:
    def __init__(self):
        self.dynamite = 100
        self.botone = []
        self.bottwo = []
        self.firsttie = 0
        self.broketie = ""
        self.wastie = False

    def make_move(self, gamestate):
        rounds = gamestate['rounds']
        length = len(rounds)

        if length == 0 or length == 1:
            return "P"

        self.botone = list(map(lambda x: x['p1'], rounds))
        self.bottwo = list(map(lambda x: x['p2'], rounds))

        if self.firsttie == 1:
            self.broketie = self.botone[length - 1]
            self.firsttie = 2

        print(self.wastie)
        # Draw
        if self.wastie:
            if self.botone[length - 1] == self.bottwo[length - 1] and ("D" in self.bottwo[length - 1]):
                print("here")
                if self.firsttie == 0:
                    self.firsttie = 1
                    self.wastie = False
                    return "W"
                else:
                    if "D" in self.broketie:
                        self.wastie = False
                        return "W"
                    elif "W" in self.broketie:
                        self.wastie = False
                        return "P"
                    else:
                        if self.dynamite > 0:
                            self.dynamite -= 1
                            self.wastie = False
                            return "D"
                        else:
                            self.wastie = False
                            return "P"
            else:
                if self.dynamite > 0:
                    self.dynamite -= 1
                    self.wastie = False
                    return "D"



        elif self.botone[length - 1] == self.bottwo[length - 1]:
            self.wastie = True
            self.firsttie = 1
            if self.dynamite > 0:
                self.dynamite -= 1
                return "D"
            else:
                return "W"

        lastmove = self.bottwo[length - 1]

        if lastmove == rounds[length - 2]['p2']:
            if lastmove == "R":
                return "P"
            elif lastmove == "S":
                return "R"
            elif lastmove == "P":
                return "S"
            else:
                return "W"
        else:
            if lastmove == "R":
                return "R"
            elif lastmove == "S":
                return "S"
            elif lastmove == "P":
                return "P"

        return "P"
