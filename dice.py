import constants as c 
from enum import Enum
import random

DEFAULT_DICE_MIN = 1
DEFAULT_DICE_MAX = 6

class Effect(Enum):
    DAMAGE = 1
    HEALING = 2
    POISON = 3

effect_text = {Effect.DAMAGE: "DAMAGE", Effect.HEALING: "HEALING",
               Effect.POISON: "POISON"}

class Result:
    def __init__(self, val: int, effect_type: Effect = Effect.DAMAGE,
                 index: int = 0):
        self.val = val
        self.effect_type = effect_type
        self.index = index

class Dice:
    def __init__(self, description: str = "A standard d6.",
                 sides : list[int] = range(DEFAULT_DICE_MIN,DEFAULT_DICE_MAX+1),
                 t: Effect = Effect.DAMAGE):
        self.sides = sides
        self.effect_type = t
        self.description = description

    def roll(self, index: int = 0):
        return Result(val = random.randint(self.min, self.max),
                       effect_type = self.effect_type,
                       index = index)

    def explain(self):
        print(f"Dice Type: {self.effect_type}")
        print(f"Number of sides: {len(self.sides)}")
        print(self.description)
        if len(self.sides) < 10:
            print(f"Possible Rolls: {' '.join(self.sides)}")
            
    def is_blank(self):
        for side in self.sides:
            if side != 0:
                return False
        return True
        

class DiceBag:
    def __init__(self, dice: list[Dice] = [Dice()]):
        self.dice = dice

    def roll(self, target_index: int = 0):
        results = []
        for d in self.dice:
            results.append(d.roll(index=target_index))
        return results
    
    def show_dice(self):
        print(f"Currently, your bag has {len(self.dice)} dice in it!")
        for i, d in enumerate(self.dice):
            print(f"Dice #{i+1}:")
            d.explain()
            
class EnemyDiceBag(DiceBag):
    def __init__(self, dice: list[Dice] = [Dice()]):
        if len(dice) != 3:
            print(f"err: An enemy must be specified by three dice. Received {len(dice)} : {dice}")
            return
        self.dice = dice
        
    def show_dice(self):
        print(f"The selected Creature's Dice Bag has {len(self.dice)} dice in it.")
        for i, d in enumerate(self.dice):
            print(f"Dice #{i+1}:")
            d.explain()