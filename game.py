from round import Round

class Game:
    def __init__(self, players):
        self.players = players
        self.round_number = 1

    def active_players(self):
        return [p for p in self.players if p.active]

    def is_over(self):
        return len(self.active_players()) <= 1

    def run(self):
        while not self.is_over():
            print(f"\n=== Round {self.round_number} ===")
            round = Round(self)
            round.play()
            self.round_number += 1
        winner = self.active_players()[0]
        print(f"The winner {winner.name} takes it all!")