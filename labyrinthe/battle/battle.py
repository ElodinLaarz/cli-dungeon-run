import time

from character.character import Alliance, Status, Character
from character.player import Player
from character.enemy import Enemy
from character.enemy_types import Rank
from dice import dice
import constants as c
import fancy_print as fp

rank_to_index = {
    Rank.VANGUARD: 0,
    Rank.SUPPORT: 1,
    Rank.CASTER: 2
}

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
        print(",\n".join(
            [x.char_hp() + f" (Speed: {x.attributes.speed})"
             for x in turns]))
        fp.Fancy_Print(f"\nRound {self.round}:\n\n" +
        f"{[x.char_hp() for x in turns]}.")
        for cur_turn_creature in turns:
            if self.battle_ended:
                return
            result = cur_turn_creature.roll()
            # CHECK FOR CONFUSION
            # APPLY FAVORABLY OR NOT
            print(f"{cur_turn_creature.name} acts!")
            time.sleep(0.5)
            self.print_roll(result)
            target_rule = Target_Rule.HEAL_PLAYER_DAMAGE_ENEMY
            if cur_turn_creature.alliance == Alliance.ENEMY:
                target_rule = Target_Rule.DAMAGE_PLAYER_HEAL_ENEMY
            self.apply(
                target_rule=target_rule,
                results=result)
            self.tidy_battlefield()
            time.sleep(2)

    def run(self) -> Status:
        while not self.battle_ended:
            self.step()
        return self.player.status()

    def print_roll(self, results: list[dice.Result]):
        for result in results:
            print(f"{result.val} " +
                  f"{dice.effect_text[result.effect_type]}")

    def apply(self,
              target_rule: Target_Rule,
              results: list[dice.Result]):
        for result in results:
            self.apply_one(
                target_rule=target_rule,
                result=result)
            self.tidy_battlefield()

    def apply_one(self,
                  target_rule: Target_Rule,
                  result: dice.Result):
        if target_rule == Target_Rule.HEAL_PLAYER_DAMAGE_ENEMY:
            if result.effect_type == dice.Effect.HEALING:
                self.player.healing(result.val)
            elif result.effect_type == dice.Effect.POISON:
                self.poison_enemy(result)
            else:
                self.damage_enemy(result)
        elif target_rule == Target_Rule.DAMAGE_PLAYER_HEAL_ENEMY:
            if result.effect_type == dice.Effect.HEALING:
                self.heal_enemy(result)
            elif result.effect_type == dice.Effect.POISON:
                self.player.poison(result.val)
            else:
                self.player.damage(result.val)

    def poison_enemy(self, poison_result: dice.Result):
        if poison_result.effect_type != dice.Effect.POISON:
            print("Healing an enemy with non-poison-type "+
                  f"{poison_result.effect_type}, {poison_result.val}")
        poison_val = poison_result.val
        self.enemies[0].poison(poison_val)


    def heal_enemy(self, heal_result: dice.Result):
        if heal_result.effect_type != dice.Effect.HEALING:
            print("Healing an enemy with non-heal-type "+
                  f"{heal_result.effect_type}, {heal_result.val}")
        heal_value = heal_result.val
        for enemy in self.enemies:
            if enemy.attributes.current_hp < enemy.attributes.max_hp:
                enemy.attributes.current_hp = min(
                    enemy.attributes.current_hp + heal_value,
                    enemy.attributes.max_hp
                )
                return
        print("All enemies already at full health.")

    def damage_enemy(self, result: dice.Result):
        effect_type = result.effect_type
        FRONT = "FRONT" # Index 0
        BACK = "BACK" # Index -1
        ALL = "ALL"
        effect_to_rank = {
            dice.Effect.AOE: ALL,
            dice.Effect.DAMAGE: FRONT,
            dice.Effect.POISON: FRONT,
            dice.Effect.SWORD_SHIELD: FRONT,
            dice.Effect.RANGED_DAMAGE: BACK,
        }
        if effect_to_rank[effect_type] == FRONT:
            self.enemies[0].damage(result.val)
        elif effect_to_rank[effect_type] == BACK:
            self.enemies[-1].damage(result.val)
        else:
            for enemy in self.enemies:
                enemy.damage(result.val)

    def tidy_battlefield(self):
        living_enemies = []
        for e in self.enemies:
            if e.status() != Status.IS_DEAD:
                living_enemies.append(e)
            else:
                print(f"{e.name} has been defeated!")
        self.enemies = living_enemies
        if self.player.status() == Status.IS_DEAD or len(self.enemies) == 0:
            self.battle_ended = True

    def turn_order(self) -> list[Character]:
        all_characters = [self.player] + self.enemies
        return sorted(
            all_characters,
            key=lambda x: x.attributes.speed,
            reverse=True)
