from round import Round

class Game:
    def __init__(self):
        self.players = None
        self.round_number = 0

    def active_players(self):
        return [p for p in self.players if p.active]

    def is_over(self):
        return len(self.active_players()) <= 1

    def run(self, players):
        self.players = players
        self.round_number = 1
        while not self.is_over():
            print(f"\n=== Round {self.round_number} ===")
            round = Round(self)
            round.play()
            self.round_number += 1
        winner = self.active_players()[0]
        print(f"The winner {winner.name} takes it all!")

    def greet_player(self):
        print("Welcome to Liar's Dice!")
        name = input("What's your name? ")
    
        while True:
            try:
                bot_count = int(input("How many bot players do you want to play against? "))
                if bot_count >= 0:
                    break
                else:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
    
        print(f"Nice to meet you, {name}!")
        print(f"Great! Starting a game with you and {bot_count} bot(s).")
        return name, bot_count