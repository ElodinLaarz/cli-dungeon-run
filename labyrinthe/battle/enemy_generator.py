import random
from character import enemy_types
from character.enemy_types import Rank
from character.enemy import Enemy
from dice.dice import Dice
from dice.dice import Effect

# NOTE: Somthing fishy going on with the generator... A floor-1 Goblin
# dealth 8 damage to me :(

base_dice = {
    Rank.VANGUARD:
        [
            Dice(
            description="d6 Damage Dice: Attacks for value rolled.",
            effect_type=Effect.DAMAGE,
            sides=list(range(1,6+1))
            ),
            Dice(
            description="d3 Sword/Shield Dice: Attack and Block " +
            "for value rolled.",
            effect_type=Effect.SWORD_SHIELD,
            sides=list(range(0,3+1))
            )
        ],
    Rank.SUPPORT:
        [
            Dice(
            description="d3 Damage Dice: A standard d3. Warning: " + 
            "Don't try to visualize in three dimensions.",
            effect_type=Effect.DAMAGE,
            sides=list(range(1,3+1))
            ),
            Dice(
            description="d4 Healing Dice: Heal front-most damaged " +
            "ally for value rolled.",
            effect_type=Effect.HEALING,
            sides=list(range(1,4+1))
            )
        ],
    Rank.CASTER:
        [
            Dice(
            description="d4 Ranged Damage Dice: Attacks rear-most " +
            "enemy for value rolled.",
            effect_type=Effect.RANGED_DAMAGE,
            sides=list(range(1,4+1))
            ),
            Dice(
            description="AOE Damage Dice: Damages all enemies for " +
            "value rolled.",
            effect_type=Effect.AOE,
            sides=[1,1,1,2,3]
            )
        ],        
    }

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

def fair_num_dice_to_roll(floor_number: int) -> int:
    # To futureproof if number of floors changes
    return min(floor_number // 5 + 1, 3)

def fair_dice(floor_number: int, rank: Rank) -> Dice:
    example_fair_dice_by_zone = random.choice(base_dice[rank])
    example_fair_dice_by_zone.rescale(1+0.2*(floor_number-1))
    return example_fair_dice_by_zone

def fair_enemy(floor_number: int, rank: Rank) -> Enemy:
    enemy_type = random.choice(
        enemy_types.creatures_by_floor(
            floor_number=floor_number,
            rank=rank
        )
    )
    dice = []
    for _ in range(fair_num_dice_to_roll(floor_number=floor_number)):
        dice.append(fair_dice(floor_number=floor_number, rank=rank))
    enemy_dice = [
        fair_dice(floor_number=floor_number, rank=rank)
        for i in range(fair_num_dice_to_roll(floor_number=floor_number))]
    return Enemy(enemy_type=enemy_type, enemy_dice=enemy_dice)

index_to_rank = {
    0: Rank.VANGUARD,
    1: Rank.SUPPORT,
    2: Rank.CASTER
}

def Enemy_Generator(floor_number: int) -> list[Enemy]:
    return [
        fair_enemy(floor_number=floor_number, rank=index_to_rank[i])
        for i in range(enemy_number(floor_number=floor_number))
    ]
