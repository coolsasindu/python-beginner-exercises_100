import random


class Dice:
    def roll(self):
        first = random.randint(1, 10)
        second = random.randint(1, 10)
        return first, second


dice = Dice()
print(dice.roll())

