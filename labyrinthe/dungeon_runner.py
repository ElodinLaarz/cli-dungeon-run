import time
import choices
from battle.battle import Battle
from battle import enemy_generator
from character import character
from character.player import Player
import character.player_classes as pc
import constants as c
import fancy_print as fp

FIGHT = "Fight"
HEAL = "HEAL to full (10G)"

in_between_round_choices = [
    HEAL,
    "Check Mercenaries",
    FIGHT,
    "Show your Character's Current Status"
]

class DungeonRun:
    def __init__(self, player_name: str):
        self.player = Player(name = player_name)
        self.battle = None
        self.floor = 1

    def setup(self):
        return

    def Start(self):
        self.setup()
        self.opening()
        new_floor = True
        while self.player.status() != character.Status.IS_DEAD and self.floor < 10:
            if new_floor:
                if self.floor == 10:
                    fp.Fancy_Print("THE FINAL FLOOR! " + 
                                   "Hope you are ready for a challenge!")
                fp.Fancy_Print(f"Welcome to Floor {self.floor}! " +
                            "Take a moment to look around...")
                new_floor = False
            choice_index = choices.get_choice(in_between_round_choices)
            choice = in_between_round_choices[choice_index]
            if choice == FIGHT:
                enemies = enemy_generator.Enemy_Generator(self.floor)
                battle = Battle(self.player, enemies=enemies)
                if battle.run() != character.Status.IS_DEAD:
                    # REWARDS AND XP
                    self.floor += 1
                    new_floor = True
                else:
                    print("Oh no! You died.")
                    print(f"You made it to floor {self.floor}.")
            elif choice == HEAL:
                if self.player.gold < 10:
                    print("Whoops... Looks like your pockets are " +
                          "a little light there. Come back when " +
                          "you have some more gold, alright?")
                    continue
                cur_hp = self.player.attributes.current_hp
                max_hp = self.player.attributes.current_hp
                if cur_hp >= max_hp:
                    print("On second thought, you realize you are " +
                          "feeling healthy enough already...\n" +
                          f"Current HP: {cur_hp}, Max HP: {max_hp}")
                

    def opening(self):
        fp.Fancy_Print(
            f"Welcome to {c.GAME_NAME}, {self.player.name}!")
        print("Choose a class!")
        chosen_index = choices.get_choice(
            [x.name for x in pc.Player_Classes])
        chosen_class = pc.Player_Classes[chosen_index]
        print(f"You have chosen {chosen_class.name}!")
        self.player.set_class(chosen_class)
        fp.Fancy_Print(
            "You will start with the following stats:\n\n" + 
            self.player.char_stats())
        time.sleep(1)
        self.refresh_screen()

    def refresh_screen(self):
        print("\r")
