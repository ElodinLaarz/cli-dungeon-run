import constants as c

from player_classes import PlayerClass
import character
from character import Character
from dice import DiceBag

class Player(Character):
    def __init__(self, db: DiceBag = DiceBag(), name: str = character.DEFAULT_NAME,
                 attributes: character.Attributes = character.Attributes()):
        super().__init__(db=db, name="PC " + name, attributes=attributes)

    def set_class(self, player_class: PlayerClass):
        self.attributes = player_class.attributes