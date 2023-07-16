from enum import Enum
import random

DEFAULT_DICE_MIN = 1
DEFAULT_DICE_MAX = 6

class Effect(Enum):
    DAMAGE = 1
    HEALING = 2
    POISON = 3
    SWORD_SHIELD = 4 # Not coded yet...
    RANGED_DAMAGE = 5
    AOE = 6

effect_text = {
    Effect.DAMAGE: "Attack",
    Effect.HEALING: "Heal",
    Effect.POISON: "Poison",
    Effect.SWORD_SHIELD: "Attack and Block",
    Effect.RANGED_DAMAGE: "Ranged Attack",
    Effect.AOE: "AOE"
}

class Result:
    def __init__(self, val: int, effect_type: Effect = Effect.DAMAGE):
        self.val = val
        self.effect_type = effect_type

class Dice:
    def __init__(
        self,
        description: str = "A standard d6.",
        effect_type: Effect = Effect.DAMAGE,
        sides : list[int] = list(range(DEFAULT_DICE_MIN,
                                  DEFAULT_DICE_MAX+1))
        ):
        self.sides = sides
        self.effect_type = effect_type
        self.description = description

    def roll(self) -> Result:
        return Result(val = random.choice(self.sides),
                       effect_type = self.effect_type)

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

    def rescale(self, scaling_factor: float):
        for index, side in enumerate(self.sides):
            self.sides[index] = int(side*scaling_factor)
