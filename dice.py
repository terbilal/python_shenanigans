#!/usr/bin/env python3
# FUCKING OOP CLASSES KYS U FUCKING OOOP SHITHEAD >~<
from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll(self):
        return randint(1,self.sides)

# Normal six sided default die
die = Die()
# 10 sides die
ten_sided_die = Die(10)
# 20 sides die
twenty_sided_die = Die(20)
# print the dice ten times each
for i in range(10):
    print(die.roll())
print()
for i in range(10):
    print(ten_sided_die.roll())
print()
for i in range(10):
    print(twenty_sided_die.roll())
