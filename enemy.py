import character
from character import Character
import dice
from enemy_types import EnemyType

class Enemy(Character):
    # def __init__(self, db: DiceBag = DiceBag(), name: str = character.DEFAULT_NAME,
    #              max_hp: int = character.DEFAULT_HEALTH, speed: int = character.DEFAULT_SPEED):
    #     super().__init__(db=db, name="NPC " + name, max_hp=max_hp, speed=speed)
    def __init__(self, enemy_type: EnemyType):
        enemy_dice = list[dice.Dice]
        if not enemy_type.damage_die.is_blank():
            enemy_dice.append(enemy_type.damage_die)
        if not enemy_type.support_die.is_blank():
            enemy_dice.append(enemy_type.support_die)
        if not enemy_type.caster_die.is_blank():
            enemy_dice.append(enemy_type.caster_die)
        if len(enemy_dice) == 0:
            print("Attempted to create enemy with no dice! PANIC!")
            return
        name = enemy_type.name
        attributes = enemy_type.attributes

        db = dice.DiceBag(enemy_dice)
        super().__init__(db=db, name="NPC " + name, attributes=attributes)
