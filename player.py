class Player:
    def __init__(self, name):
        self.name = name
        self.dice = []
        self.active = True

    def roll_dice(self):
        from random import randint
        self.dice = [randint(1, 6) for _ in range(len(self.dice))]

    def make_move(self, current_bid, total_players):
        #TODO
        pass

    def challenge(self):
        #TODO
        pass

class BotPlayer(Player):
    def make_move(self, current_bid, total_players):
        #TODO
        pass