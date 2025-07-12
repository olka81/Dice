from player import Player, BotPlayer

players = [Player("You"), BotPlayer("Bot1"), BotPlayer("Bot2")]

for player in players:
    player.dice = [0] * 5 
    player.roll_dice()