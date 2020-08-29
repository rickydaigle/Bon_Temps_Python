#!/usr/bin/env python3

# This module allows for a battle system

# To use this module:
# 1.) from features.battlesystem import Battle
# 2.) use class functions as needed - pretty straightforward

import random
import time

class Battle:

    def begin_battle(player, mob, totalAttack, totalDefense):
        """
        Begins a battle between the player and a mob.
        """
        battle = True
        print()
        print("A battle has begun!")
        while battle:
            if player.player_alive():
                print()
                time.sleep(1)
                missChance = random.random()
                if missChance > mob.get_defense_chance():
                    attackSuccess = random.random()
                    defenseSuccess = random.random()
                    damageToMob = int(round(((totalAttack * (attackSuccess * 2)) + int(player.get_level())) - ((int(mob.get_defense()) * defenseSuccess) + int(mob.get_level()))))
                    if damageToMob > 0:
                        print("You {} the {} for {} damage!".format(player.get_attack_verb(), mob.print_name(), damageToMob))
                        mob.lose_health(damageToMob)
                    else:
                        print("Your {} missed!".format(player.get_attack_verb()))
                else:
                    print("The {} managed to {} your {}!".format(mob.print_name(), mob.get_defense_verb(), player.get_attack_verb()))
                if mob.mob_alive():
                    time.sleep(1)
                    if missChance > player.get_defense_chance():
                        attackSuccess = random.random()
                        defenseSuccess = random.random()
                        damageToPlayer = int(round(((totalAttack * (attackSuccess * 1.5)) + int(player.get_level())) - ((int(mob.get_defense()) * defenseSuccess) + int(mob.get_level()))))
                        if damageToPlayer > 0:
                            print("The {} {}s you for {} damage!".format(mob.print_name(), mob.get_attack_verb(), damageToPlayer))
                            player.lose_health(damageToPlayer)
                        else:
                            print("The {}'s {} missed!".format(mob.print_name() ,mob.get_attack_verb()))
                    else:
                        print("You managed to {} the {}'s {}!".format(player.get_defense_verb(), mob.print_name(), mob.get_attack_verb()))
                    print("Your health: {}".format(player.get_health()))
                else:
                    Battle.battle_won(player, mob)
                    battle = False
            else:
                Battle.battle_lost(player, mob)
                battle = False

    def battle_won(player, mob):
        print("You have killed the {}!".format(mob.print_name()))
        newExp = mob.get_exp()
        newCurrency = mob.get_bones()
        player.killed_enemy()
        print("Your kill total is now {}.".format(player.get_total_kills()))
        print("You've earned {} experience points and found {} bones!".format(newExp, int(newCurrency)))
        player.gain_exp(newExp)
        player.gain_currency(newCurrency)

    def battle_lost(player, mob):
        print("The {} has killed you.".format(mob.print_name()))


def unit_test():

    input("Press Enter to exit test...")

if __name__ == "__main__":
    unit_test()

