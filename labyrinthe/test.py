import os
import sys

# fpath = os.path.join(os.path.dirname(__file__), 'dice')
# sys.path.append(fpath)
# print(sys.path)

from dice.dice import Dice

print(Dice().explain())