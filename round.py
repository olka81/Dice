from settings import DEBUG
from player import BotPlayer

class Round:
    def __init__(self, game):
        self.game = game
        self.players = game.active_players()
        self.current_bid = None
        self.current_bidder = None

    def play(self):
        #TODO think about change of first player
        for p in self.players:
            p.roll_dice()

        if DEBUG:
            print("\nDEBUG: All dices:")
            for p in self.players:
                print(f"{p.name}: {p.dice}")
                if isinstance(p, BotPlayer):
                    print(f"aggression level {p.aggression_level}, bluff chance: {p.bluff_chance}")

        idx = 0
        while True:
            player = self.players[idx % len(self.players)]

            move = player.make_move(self.current_bid, sum(len(p.dice) for p in self.players))

            if move == 'liar':
                print(f"\n{player.name} call 'liar' {self.current_bidder.name} with {self.current_bid}")
                total = sum(p.count_matching(self.current_bid[1]) for p in self.players)
                print(f"Found: {total}")

                if total >= self.current_bid[0]:
                    print(f"{player.name} made mistake and loses dice.")
                    player.lose_die()
                else:
                    print(f"{self.current_bidder.name} lied and loses dice.")
                    self.current_bidder.lose_die()
                break
            else:
                self.current_bid = move
                self.current_bidder = player
                print(f"{player.name} highers up to {self.current_bid}")
                idx += 1