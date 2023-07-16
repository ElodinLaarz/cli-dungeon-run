from enemy_types import EnemyType
from character.character import Character
from dice import dice

class Enemy(Character):
    def __init__(
        self,
        enemy_type: EnemyType,
        enemy_dice: dice.DiceBag
        ):
        name = enemy_type.name
        attributes = enemy_type.attributes
        dice_bag = dice.DiceBag(enemy_dice)

        super().__init__(
            dice_bag=dice_bag,
            name="NPC " + name,
            attributes=attributes)
