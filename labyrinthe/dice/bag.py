from dice.dice import Dice, Result

class DiceBag:
    def __init__(
        self,
        dice: list[Dice] = None):
        self.dice = dice

    def roll(self) -> list[Result]:
        return [die.roll() for die in self.dice]

    def show_dice(self):
        print(f"Currently, your bag has {len(self.dice)} dice in it!")
        for i, die in enumerate(self.dice):
            print(f"Dice #{i+1}:")
            die.explain()

class EnemyDiceBag(DiceBag):
    def show_dice(self):
        print(f"The selected Creature's Dice Bag has {len(self.dice)} dice in it.")
        for i, die in enumerate(self.dice):
            print(f"Dice #{i+1}:")
            die.explain()
