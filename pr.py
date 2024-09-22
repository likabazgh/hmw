import random

players = int(input("enter players number: "))

for i in range(0, players):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(f"{die1} {die2}")