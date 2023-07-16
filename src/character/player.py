from player_classes import PlayerClass
import character.character as character
from character.character import Character
from dice.dice import Dice
from dice.dice import DiceBag

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

    def set_class(self, player_class: PlayerClass):
        self.attributes = player_class.attributes
