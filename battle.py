import character
from character import Character
import constants as c
import dice as d
from enum import Enum
import fancy_print as fp
from player import Player
from enemy import Enemy

class Target_Rule:
    HEAL_PLAYER_DAMAGE_ENEMY = 1
    DAMAGE_PLAYER_HEAL_ENEMY = 2

class Battle:
    def __init__(self, player : Player, enemies: list[Enemy]):
        self.player = player
        self.enemies = enemies
        self.round = 0
        self.battle_ended = False

    def step(self):
        self.round += 1
        turns = self.turn_order()
        fp.Fancy_Print(f"\nRound {self.round}:\n\n {c.NEW_LINE_COMMA.join([x.char_hp() for x in turns])}.")
        for cur_turn_creature in turns:
            roll = cur_turn_creature.roll()
            # CHECK FOR CONFUSION
            # APPLY FAVORABLY OR NOT
            self.print_roll(roll)
            self.apply(roll)
            self.tidy_battlefield()
    
    def battle(self) -> bool:
        while not self.battle_ended:
            self.step()
        return self.player.status()

    def print_roll(self, roll: list[d.Result]):
        for r in roll:
            print(f"{r.val} {d.effect_text[r.effect_type]}")

    def apply(self, target_rule: Target_Rule, roll: list[d.Result]):
        for r in roll:
            self.apply_one(r)
            self.tidy_battlefield()
    
    def apply_one(self, target_rule: Target_Rule, result: d.Result):
        if target_rule == Target_Rule.HEAL_PLAYER_DAMAGE_ENEMY:
            if result.effect_type == d.Effect.HEALING:
                self.player.apply(result)
            else:
                self.enemies[result.index].apply(result)
        elif target_rule == Target_Rule.DAMAGE_PLAYER_HEAL_ENEMY:
            if result.effect_type == d.Effect.HEALING:
                self.enemies[result.index].apply(result)
            else:
                self.player.apply(result)
    
    def tidy_battlefield(self):
        living_enemies = []
        for e in self.enemies:
            if e.status() != character.Status.IS_DEAD:
                living_enemies.append(e)
            else:
                print(f"{e.name} has been defeated!")
        self.enemies = living_enemies
        if self.player.status() == character.Status.IS_DEAD or len(self.enemies) == 0:
            self.battle_ended = True        

    def turn_order(self) -> list[Character]:
        all = [self.player] + self.enemies
        return sorted(all, key=lambda x: x.speed, reverse=True)