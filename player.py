import random
from collections import Counter
from settings import USE_JOKERS

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0] * 5  # start with 5 dice
        self.counter = None
        self.active = True

    def roll_dice(self):
        self.dice = [random.randint(1, 6) for _ in self.dice]
        self.counter = Counter(self.dice)

    def count_matching(self, value):
        if USE_JOKERS:
            return sum(1 for d in self.dice if d == value or d == 1)
        else:
            return sum(1 for d in self.dice if d == value)

    def lose_die(self):
        if self.dice:
            self.dice.pop()
            self.counter = Counter(self.dice)
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
        best_value = None
        best_count = -1
        for value, count in self.counter.items():
            if count > best_count:
                best_value = value
                best_count = count

        others = total_dice - len(self.dice)
        expected_others = others / 6
        count = max(1, best_count + int(expected_others))

        return (count, best_value)   
    
class HumanPlayer(Player):
    def make_move(self, current_bid, total_dice):
        print(f"\nYour dice: {self.dice}")
        
        if current_bid:
            print(f"Current bid is: {current_bid[0]} × {current_bid[1]}'s")
        else:
            print("No current bid — you're going first!")

        while True:
            user_input = input("Enter your move ('count value' or 'liar'): ").strip().lower()

            if user_input == "liar":
                if current_bid is None:
                    print("There's nothing to challenge yet. Please make a bid.")
                    continue
                return "liar"

            parts = user_input.split()
            if len(parts) != 2:
                print("Invalid input. Enter two numbers like '3 5' or type 'liar'.")
                continue

            try:
                count = int(parts[0])
                value = int(parts[1])

                if count < 1 or value < 1 or value > 6:
                    print("Count must be ≥ 1, and value must be between 1 and 6.")
                    continue

                if current_bid and not self._is_higher_bid(current_bid, (count, value)):
                    print("Your bid must be higher than the current one.")
                    continue

                return (count, value)

            except ValueError:
                print("Invalid input. Please enter two numbers like '3 5' or type 'liar'.")

    def _is_higher_bid(self, current, new):
        curr_count, curr_value = current
        new_count, new_value = new
        return new_count > curr_count or (new_count == curr_count and new_value > curr_value)