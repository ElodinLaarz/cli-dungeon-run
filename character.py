import constants as c
from enum import Enum
import dice as d

DEFAULT_HEALTH = 10
DEFAULT_NAME = "unnamed"
DEFAULT_SPEED = 3
DEFAULT_TOUGHNESS = 0

class Attributes:
    def __init__(self, max_hp: int = DEFAULT_HEALTH, speed: int = DEFAULT_SPEED, toughness: int = DEFAULT_TOUGHNESS):
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.toughness = toughness
        self.speed = speed

class Status(Enum):
    IS_DEAD = 1
    IS_ALIVE = 2

class Character:
    def __init__(self, db: d.DiceBag = d.DiceBag(), name: str = DEFAULT_NAME,
                 attributes: Attributes = Attributes(current_health=DEFAULT_HEALTH,
                                                    max_hp=DEFAULT_HEALTH,
                                                    toughness=DEFAULT_TOUGHNESS,
                                                    speed=DEFAULT_SPEED)):
        self.name = name
        self.attributes = attributes
        self.db = db
        self.poison_val = 0

    def turn_start(self) -> c.Status:
        if self.poison_val > 0:
            self.damage(self.poison_val)
            self.poison_val -= 1
        return self.status()

    def is_alive(self) -> bool:
        return self.current_health > 0

    def damage(self, val: int) -> Status:
        self.current_health -= val
        return self.status()
    
    def healing(self, val: int) -> Status:
        self.current_health = min(self.attributes.max_hp,self.current_health+val)
        return self.status()

    def poison(self, val: int) -> Status:
        self.poison_val += val
        return self.status()

    def apply(self, result: d.Result) -> Status:
        dt = result.effect_type
        if dt == d.Effect.DAMAGE:
            return self.damage(result.val)
        elif dt == d.Effect.HEALING:
            return self.healing(result.val)
        elif dt == d.Effect.POISON:
            return self.poison(result.val)
        print(f"Uh Oh... Unexpected damage type {dt}.")

    def roll(self):
        return self.db.roll(targeting=self.targeting)

    def status(self):
        if self.is_alive():
            return Status.IS_ALIVE
        return Status.IS_DEAD

    def char_hp(self) -> str:
        return f"{self.name}: HP {self.current_health} / {self.attributes.max_hp}"

    def char_stats(self) -> str:
        return f"""{self.name}:
HP {self.attributes.current_hp} / {self.attributes.max_hp}
Toughness {self.attributes.toughness} (Relates to defense and HP regen)
Speed {self.attributes.speed} (Determines turn order and dodge chance)"""
