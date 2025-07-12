import random
from settings import USE_JOKERS

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0] * 5  # start with 5 dice
        self.active = True

    def roll_dice(self):
        self.dice = [random.randint(1, 6) for _ in self.dice]

    def count_matching(self, value):
        if USE_JOKERS:
            return sum(1 for d in self.dice if d == value or d == 1)
        else:
            return sum(1 for d in self.dice if d == value)

    def lose_die(self):
        if self.dice:
            self.dice.pop()
        if not self.dice:
            self.active = False

    def make_move(self, current_bid, total_dice):
        raise NotImplementedError

    def __str__(self):
        return f"{self.name} ({len(self.dice)} dice)"


class BotPlayer(Player):
   
    def make_move(self, current_bid, total_dice):
        count, value = current_bid if current_bid else self.make_first_bid(total_dice)
        estimate = total_dice // 3

        if count >= estimate + 2:
            return 'liar'

        if value < 6:
            return (count, value + 1)
        else:
            return (count + 1, 2)
    
    def make_first_bid(self, total_dice):
        from collections import Counter

        counter = Counter(self.dice)
        best_value = max(counter.items(), key=lambda x: x[1])[0]
        my_count = counter[best_value]

        others = total_dice - len(self.dice)
        expected_others = others / 6
        count = max(1, my_count + int(expected_others))

        return (count, best_value)   
