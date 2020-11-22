###### Step 1: Create an environment for a 1 on 1 battle ######

# Code below expands on the initial starting code made by Ryan Fowers: https://github.com/rylanpfowers/YouTube/blob/master/pokemon.py

# Import existing libraries  needed for the game
import time
import numpy as np
import sys

# Import libraries that I made to make the game run
from battle_functions import damage_step, delay_print, pokemon_move_script

# Instantiate a pokemon class, from which the battle and pokemon objects can be determined
class Pokemon:
    # Initiate the pokemon class to be developed
    def __init__(self, 
                 name,  # name of the first pokemon
                 types, # first pokemon types
                 level, # first pokemon level
                 moves, # moves that the first pokemon has
                 EVs):  # attack, defense, health and speed stats

        # save self pokemon attributes as variables
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.speed = EVs['SPEED']
        self.health = EVs['HEALTH']
        self.level = level

    # Definition that causes pokemon to fight
    def fight(self, Pokemon2):
        # Print fight information
        print("-----POKEMON BATTLE-----")

        # Pokemon 1 (Self)
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("HEALTH/", self.health)
        print("LVL/", self.level) #3*(1+np.mean([self.attack,self.defense])))

        print("\nVS")

        # Pokemon 2 (Opponent)
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)
        print("SPEED/",Pokemon2.speed)
        print("HEALTH/", Pokemon2.health)
        print("LVL/", Pokemon2.level)
        time.sleep(2)

        # Calculation of damage modification due to type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k: #identifies the type of the self pokemon
                # Both are same type
                if Pokemon2.types == k: #if opponent pokemon is the same type
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is STRONG
                if Pokemon2.types == version[(i+1)%3]: #Pokemon is the next-up/strong in the type hierarchy (if the index exceeds 3, the modulus 3 reverts it back to next-position in list)
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    #self.attack /= 2
                    #self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is WEAK
                if Pokemon2.types == version[(i+2)%3]: #Pokemon is the next-down/weak in the type hierarchy (if the index exceeds 3, the modulus 3 reverts it back to lesser-position in list)
                    self.attack *= 2
                    self.defense *= 2
                    #Pokemon2.attack /= 2
                    #Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'

        #-------- DESIGN OF THE ACTUAL POKEMON FIGHT ----------------
        move_count = 0

        # This script continues while a pokemon has the ability to still fight (i.e. still has health)
        while (self.health > 0) and (Pokemon2.health > 0):
            # Move count increases by 1 increment
            move_count+=1

            # Print the health of each pokemon
            print(f'\n----------------- MOVE {move_count} ------------------')
            print(f"\n{self.name}\t\tHEALTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHEALTH\t{Pokemon2.health}\n")

            # Create the selection of moves for Pokemon 1
            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index_self = int(input('Pick a move: '))
            self_move_name = list(self.moves.keys())[index_self-1]
            time.sleep(1)

            # Move selection of pokemon 2
            print(f"\nGo {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index_2 = int(input('Pick a move: '))
            pokemon2_move_name = list(Pokemon2.moves.keys())[index_2-1]

            # Move and damage criteria for self pokemon and Pokemon 2, respectively
            self_damage_dealt = damage_step(self.level,self.moves[self_move_name],self.attack,self.defense)            
            pokemon2_damage_dealt = damage_step(Pokemon2.level,Pokemon2.moves[pokemon2_move_name],Pokemon2.attack,Pokemon2.defense)
            print(self_damage_dealt, pokemon2_damage_dealt)

            time.sleep(1)

            if self.speed > Pokemon2.speed:
                #-------- ATTACK OF POKEMON 1 AGAINST POKEMON 2 ------------
                self.health, Pokemon2.health = pokemon_move_script(self.name, self.health, self_move_name, string_1_attack, self_damage_dealt, Pokemon2.name, Pokemon2.health)
                if Pokemon2.health <= 0:
                    delay_print("\n..." + Pokemon2.name + ' fainted.')
                    break
                
                #-------------- ATTACK OF POKEMON 2 AGAINST POKEMON 1 -------------
                Pokemon2.health, self.health = pokemon_move_script(Pokemon2.name, Pokemon2.health, pokemon2_move_name, string_2_attack, pokemon2_damage_dealt, self.name, self.health)
                if self.health <= 0:
                    delay_print("\n..." + self.name + ' fainted.')
                    break

            else:
                #-------------- ATTACK OF POKEMON 2 AGAINST POKEMON 1 -------------
                Pokemon2.health, self.health = pokemon_move_script(Pokemon2.name, Pokemon2.health, pokemon2_move_name, string_2_attack, pokemon2_damage_dealt, self.name, self.health)
                if self.health <= 0:
                    delay_print("\n..." + self.name + ' fainted.')
                    break

                #-------- ATTACK OF POKEMON 1 AGAINST POKEMON 2 ------------
                self.health, Pokemon2.health = pokemon_move_script(self.name, self.health, self_move_name, string_1_attack, self_damage_dealt, Pokemon2.name, Pokemon2.health)
                if Pokemon2.health <= 0:
                    delay_print("\n..." + Pokemon2.name + ' fainted.')
                    break

        money = np.random.choice(5000)
        delay_print(f"\nOpponent paid you ${money}.\n")




if __name__ == '__main__':
    #Create Pokemon
    Charizard = Pokemon('Charizard', 'Fire', 50, {'Flamethrower':95, 'Fire Blast':110, 'Blast Burn':150, 'Fire Punch':75}, {'ATTACK':12, 'DEFENSE': 80, 'SPEED': 16, 'HEALTH': 30})
    Blastoise = Pokemon('Blastoise', 'Water', 50, {'Water Gun':40, 'Bubblebeam':65, 'Hydro Pump':110, 'Surf':85},{'ATTACK': 10, 'DEFENSE':10, 'SPEED': 18, 'HEALTH': 30})
    Venusaur = Pokemon('Venusaur', 'Grass', 50, ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12, 'SPEED': 14, 'HEALTH': 100})

    Charmander = Pokemon('Charmander', 'Fire', 50, ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2, 'SPEED': 8, 'HEALTH': 100})
    Squirtle = Pokemon('Squirtle', 'Water', 50, ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3, 'SPEED': 9, 'HEALTH': 100})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', 50, ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4, 'SPEED': 7, 'HEALTH': 100})

    Charmeleon = Pokemon('Charmeleon', 'Fire', 50, ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5, 'SPEED': 31, 'HEALTH': 100})
    Wartortle = Pokemon('Wartortle', 'Water', 50, ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5, 'SPEED': 4, 'HEALTH': 100})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', 50, ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6, 'SPEED': 3, 'HEALTH': 100})

    Charizard.fight(Blastoise) # Get them to fight