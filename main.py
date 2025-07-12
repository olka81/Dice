from player import BotPlayer
from game import Game

players = [
    BotPlayer("Bot A"),
    BotPlayer("Bot B"),
    BotPlayer("Bot C")
]

game = Game(players)
game.run()