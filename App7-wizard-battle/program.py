#!/Users/norbertkirkpatrick/Documents/Python/Python-Build-10Apps/App7-wizard-battle/venv/bin/python

from actors import Wizard, Creature, SmallAnimal, Dragon
import random
import time

def main():
    print_header()
    game_loop()

def print_header():
    print('-------------------------------')
    print('        Wizard Game App')
    print('-------------------------------')
    print()

def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Creature('Evil Wizard', 1000)
    ]

    # print(creatures)

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))

        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides to recover...")
                time.sleep(5)
                print("Thie wizard returns revitalized!")
        elif cmd == 'r':
            print("The wizard has become unsure of his powers and flees")
        elif cmd =='l':
            print("The wizard {} takes in the surroundings and sees:".format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('Ok, exiting game... bye!')
            break

        if not creatures:
            print("You defeated all the creatures, well done!")

        
if __name__ == '__main__':
    main()