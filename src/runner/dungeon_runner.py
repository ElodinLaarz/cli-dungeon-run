import time
from player import Player
import player_classes as pc
from runner import choices
from battle.battle import Battle
from battle.enemy_generator import Enemy_Generator
from character import character
import constants as c
import fancy_print as fp

FIGHT = "Fight"

in_between_round_choices = ["HEAL to full (10G)", "Check Mercenaries", FIGHT]

class DungeonRun:
    def __init__(self, player_name: str):
        self.player = Player(name = player_name)
        self.battle = None
        self.floor = 0

    def setup(self):
        return

    def Start(self):
        self.setup()
        self.opening()
        while self.player.status() != character.Status.IS_DEAD and self.floor < 10:
            self.floor += 1
            if self.floor == 10:
                fp.Fancy_Print("THE FINAL FLOOR! "
                               +"Hope you are ready for a challenge!")
            fp.Fancy_Print(f"Welcome to Floor {self.floor}! " +
                           "Take a moment to look around...")
            choice_index = choices.get_choice(in_between_round_choices)
            choice = in_between_round_choices[choice_index]
            if choice == FIGHT:
                # Generate a battle based on the current floor
                # Start battle manager
                # Get Rewards / XP
                enemies = Enemy_Generator(self.floor)
                battle = Battle(self.player, enemies=enemies)
                battle.run()

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
