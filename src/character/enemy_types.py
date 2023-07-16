# Themed enemies
# Enemies with different dice types
# Enemies based on order in Combat
# (soldier front, support middle, caster back)
from enum import Enum
from character import character

class CreatureType(Enum):
    # Early Floors -- Forest
    GOBLIN = 1
    # Mid Floors -- Mountains
    TROLL = 2
    # End Floors -- Volcano
    ELEMENTAL = 3
    # Boss Floor -- Based on Boss
    DRAGON = 4

class Rank(Enum):
    VANGUARD = 1
    SUPPORT = 2
    CASTER = 3

# What does a creature type do?
# e.g. Trolls have 'fewer-sided' dice
# Dragons get +1 damage dice

class EnemyType:
    def __init__(self,
                 name: str,
                 creature_type: CreatureType,
                 starting_attributes: character.Attributes,
                 rank: Rank):
        self.name = name
        self.attributes = starting_attributes
        self.creature_type = creature_type
        self.rank = rank

enemy_types = {
    "Goblin Soldier":
        EnemyType(
            name="Goblin Soldier",
            creature_type=CreatureType.GOBLIN,
            starting_attributes=character.Attributes(
                max_hp=character.DEFAULT_HEALTH-2,
                speed=character.DEFAULT_SPEED+2,
                toughness= 0),
            rank=Rank.VANGUARD
        ),
    "Troll Shaman": 
        EnemyType(
            name="Troll Shaman",
            creature_type=CreatureType.TROLL,
            starting_attributes=character.Attributes(),
            rank=Rank.SUPPORT
        ),
    "Elemental Mage":
        EnemyType(
            name="Elemental Mage",
            creature_type=CreatureType.ELEMENTAL,
            starting_attributes=character.Attributes(
                max_hp=character.DEFAULT_HEALTH+1,
                speed=character.DEFAULT_SPEED-1,
                toughness= 1),
            rank=Rank.CASTER
        ),
    "Dragon":
        EnemyType(
            name="Dragon",
            creature_type=CreatureType.DRAGON,
            starting_attributes=character.Attributes(
                max_hp=character.DEFAULT_HEALTH*2,
                speed=character.DEFAULT_SPEED+2,
                toughness=character.DEFAULT_TOUGHNESS*2),
            rank=Rank.VANGUARD
        )
}

def creatures_by_floor(floor_number: int,
                       rank : Rank) -> list[EnemyType]:
    """Creatures by floor will return a list of 'themed' creatures
    that can be placed in the requested rank. This creature will be a
    'base' version of the creature, and will require some additional
    balancing by the caller.

    Args:
        floor_number (int): the floor of the dungeon that the creature
        should be generated for.
        rank (Rank): specifies the rank of the creature, e.g.
        Vanguard, if the requester wants to limit the creatures
        to those that should be in the front row.

    Returns:
        list[EnemyType]: themed creatures that can be placed into the
        desired rank.
    """
    if floor_number <= 3:
        creatures = [enemy_types["Goblin Soldier"]]
    elif 3 < floor_number <= 7:
        creatures = [enemy_types["Troll Shaman"],
                enemy_types["Elemental Mage"]]
    else:
        creatures = [enemy_types["Dragon"]]
    return [creature for creature in creatures if creature.rank==rank]
