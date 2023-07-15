# Themed enemies
# Enemies with different dice types
# Enemies based on order in Combat (soldier front, support middle, caster back)
import character
import dice
from enum import Enum

class CreatureType(Enum):
    # Early Floors -- Forest
    GOBLIN = 1
    # Mid Floors -- Mountains
    Troll = 2
    # End Floors -- Volcano
    Elemental = 3
    # Boss Floor -- Based on Boss
    Dragon = 4

# What does a creature type do?
# e.g. Trolls have 'fewer-sided' dice
# Dragons get +1 damage dice

class EnemyType:
    def __init__(self, name: str, creature_type: CreatureType, damage_die: dice.Dice, support_die: dice.Dice, caster_die: dice.Dice, starting_attributes: character.Attributes):
        self.name = name
        self.creature_type = creature_type
        self.damage_die = damage_die
        self.support_die = support_die
        self.caster_die = caster_die
        self.attributes = starting_attributes
        
 = [EnemyType("Soldier", character.Attributes(max_hp=character.DEFAULT_HEALTH-2, speed=character.DEFAULT_SPEED+2, toughness= 0)),
                  EnemyType("Shaman", character.Attributes()),
                  EnemyType("Warrior", character.Attributes(max_hp=character.DEFAULT_HEALTH+1, speed=character.DEFAULT_SPEED-1, toughness= 1))]