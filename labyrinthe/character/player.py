from character import character
from character.character import Character
from character.player_classes import PlayerClass
from dice.dice import Dice
from dice.bag import DiceBag

class Player(Character):
    def __init__(
        self,
        dice_bag: DiceBag = DiceBag([Dice()]),
        name: str = character.DEFAULT_NAME,
        attributes: character.Attributes = character.Attributes()):
        super().__init__(
            dice_bag=dice_bag,
            name="PC " + name,
            attributes=attributes,
            alliance=character.Alliance.FRIENDLY
        )
        self.gold = 100

    def set_class(self, player_class: PlayerClass):
        self.attributes = player_class.attributes

    def char_stats(self) -> str:
        stats = super().char_stats()
        stats += "\n" + f"Current Gold: {self.gold}"
        return stats
