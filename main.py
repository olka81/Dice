from player import BotPlayer, HumanPlayer
from game import Game


game = Game()
(name, bot_count) = game.greet_player()

players = []

players.append(HumanPlayer(name))
for i in range(bot_count):
    players.append(BotPlayer(f"Bot {i + 1}"))

game.run(players)