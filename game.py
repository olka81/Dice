import random

number = random.randint(1, 100)

print("I puzzled a number!")
p1 = int(input("Player 1:"))
p2 = int(input("Player 2:"))

d1 = abs(number - p1)
d2 = abs(number - p2)

print(f"The answer is: {number}")

if d1 < d2:
    print("Congrats, Player1")
elif d2 < d1:
    print("Congrats, Player2")
else :
    print("You both win!")