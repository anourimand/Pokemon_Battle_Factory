import time
import numpy as np
import sys

# Creates the delayed printing that exists in the traditional pokemon games
def delay_print(s): 
    # print one character at a time
    # https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# Function that calculates the damage done to a pokemon based on the move power, level, attack and defense
def damage_step(level, power, atk, defense): 
    damage = int(2+((0.4*level+2)*power*(atk/defense)/50))
    return damage

# Function that displays and updates variables as pokemon declare their moves in the battle series
def pokemon_move_script(attacker_name, attacker_health, attacker_move, attack_string, attacker_damage_dealt, opp_name, opp_health): 
    #-------- ATTACK OF POKEMON 1 AGAINST POKEMON 2 ------------
    delay_print(f"\n{attacker_name} used {attacker_move}!\n")
    delay_print(attack_string + '\n')

    # Determine damage and new health against pokemon 2
    opp_health -= attacker_damage_dealt
    if opp_health < 0:
        opp_health = 0

    # Status for Pokemon 2
    time.sleep(0.5)
    print(f"\n{attacker_name}\t\tHEALTH\t{attacker_health}")
    print(f"{opp_name}\t\tHEALTH\t{opp_health}\n")
    time.sleep(.5)

    return (attacker_health, opp_health)
