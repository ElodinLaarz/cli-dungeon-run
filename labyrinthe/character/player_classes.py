from character import character


class PlayerClass:
    def __init__(self,
                 name: str,
                 starting_attributes: character.Attributes):
        self.name = name
        self.attributes = starting_attributes


Player_Classes = [
    PlayerClass("Assassin",
                character.Attributes(
                    max_hp=character.DEFAULT_HEALTH-2,
                    speed=character.DEFAULT_SPEED+2,
                    toughness=0)),
    PlayerClass("Boring Bob",
                character.Attributes()),
    PlayerClass("Warrior",
                character.Attributes(
                    max_hp=character.DEFAULT_HEALTH+1,
                    speed=character.DEFAULT_SPEED-1,
                    toughness=1))
]
