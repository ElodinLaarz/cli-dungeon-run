from enum import Enum

from dice import dice
from dice.bag import DiceBag

DEFAULT_HEALTH = 10
DEFAULT_NAME = "unnamed"
DEFAULT_SPEED = 3
DEFAULT_TOUGHNESS = 0

class Attributes:
    def __init__(
        self,
        max_hp: int = DEFAULT_HEALTH,
        speed: int = DEFAULT_SPEED,
        toughness: int = DEFAULT_TOUGHNESS):
        self.max_hp = max_hp
        self.toughness = toughness
        self.speed = speed

class Alliance(Enum):
    FRIENDLY = 1
    ENEMY = 2

class Status(Enum):
    IS_DEAD = 1
    IS_ALIVE = 2

class Character:
    def __init__(
        self,
        dice_bag: DiceBag = DiceBag([dice.Dice()]),
        name: str = DEFAULT_NAME,
        attributes:
            Attributes = Attributes(
                max_hp=DEFAULT_HEALTH,
                toughness=DEFAULT_TOUGHNESS,
                speed=DEFAULT_SPEED),
        alliance: Alliance = Alliance.ENEMY):
        self.name = name
        self.current_hp = attributes.max_hp
        self.attributes = attributes
        self.dice_bag = dice_bag
        self.alliance = alliance
        self.poison_val = 0

    def turn_start(self) -> Status:
        if self.poison_val > 0:
            self.damage(self.poison_val)
            self.poison_val -= 1
        return self.status()

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def damage(self, val: int) -> Status:
        self.current_hp -= val
        return self.status()

    def healing(self, val: int) -> Status:
        self.current_hp = min(
            self.attributes.max_hp,
            self.current_hp+val)
        return self.status()

    def poison(self, val: int) -> Status:
        self.poison_val += val
        return self.status()

    def roll(self) -> list[dice.Result]:
        return self.dice_bag.roll()

    def status(self):
        if self.is_alive():
            return Status.IS_ALIVE
        return Status.IS_DEAD

    def char_hp(self) -> str:
        return f"{self.name}: HP {self.current_hp} / {self.attributes.max_hp}"

    def char_stats(self) -> str:
        return f"""{self.name}:
HP {self.current_hp} / {self.attributes.max_hp}
Toughness {self.attributes.toughness} (Relates to defense and HP regen)
Speed {self.attributes.speed} (Determines turn order and dodge chance)"""
