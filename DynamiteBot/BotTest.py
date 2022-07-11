class BotTest:
    def __init__(self):
        pass

    def make_move(self, gamestate):
        print(gamestate.getRounds())
        rounds = gamestate.getRounds()
        return self.solveAction(self, len(rounds), rounds)

    def solveAction(self, length, rounds):
        if length == 0 or length == 1:
            return "P"

        lastmove = rounds[length- 1].getP2()
        if lastmove == rounds[length - 2].getP2():
            if lastmove == "R":
                return "P"
            elif lastmove == "S":
                return "R"
            elif lastmove == "P":
                return "S"
        else:
            if lastmove == "R":
                return "S"
            elif lastmove == "S":
                return "P"
            elif lastmove == "P":
                return "R"





