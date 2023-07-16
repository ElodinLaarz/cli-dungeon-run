from character.enemy_types import EnemyType
from character.character import Character
from dice.bag import DiceBag

class Enemy(Character):
    def __init__(
        self,
        enemy_type: EnemyType,
        enemy_dice: DiceBag
        ):
        name = enemy_type.name
        attributes = enemy_type.attributes
        dice_bag = DiceBag(enemy_dice)

        super().__init__(
            dice_bag=dice_bag,
            name="NPC " + name,
            attributes=attributes)
