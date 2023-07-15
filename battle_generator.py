from dice import Dice
from enemy_types import EnemyType
from enemy import Enemy
from enum import Enum
import random

class Rank(Enum):
    Vanguard = 1
    Support = 2
    Caster = 3

def enemy_number(floor_number: int) -> int:
    if floor_number < 3:
        return 1
    if floor_number == 3:
        return 2
    if 3 < floor_number < 5:
        return random.choice([1, 2])
    if 5 <= floor_number < 7:
        return random.choice([1, 2, 3])
    if floor_number == 7:
        return 3
    if 7 < floor_number <= 9:
        return random.choice([2, 3])
    return 3

def fair_num_dice_to_roll(floor_num: int) -> int:
    return min(floor_num // 5 + 1, 3) # To futureproof if number of floors changes

def fair_dice(floor_num: int) -> Dice:
    example_fair_dice_by_zone = 
    return None

def fair_enemy(floor_num: int, rank: Rank) -> Enemy:
    if fair_num_dice_to_roll(floor_num) == 1
    
    return Enemy(EnemyType)

def Battle_Generator(floor_number: int) -> list[Enemy]:
    num_enemies = enemy_number(floor_number=floor_number)