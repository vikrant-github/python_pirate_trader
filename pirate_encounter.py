import random
class PirateEncounter(object):
    def __init__(self,game):
        self.game = game
        self.pirate_risk = 25
        self.pirate_strength =10
        self.chance_for_escape = 33
        self.check_for_pirates()
    
    def check_for_pirates(self):
        result = random.randint(0, 100)
        if result <= self.pirate_risk:
            self.pirate_attack()
    
    def pirate_attack(self):
        print("**************************************")
        print("****************PIRATES!!*************")
        print("**************************************")
        self.number_of_pirates = random.randint(1,self.pirate_strength)
        FightingPirates = True
        while FightingPirates:
            print("************************************")
            print("There are %s pirates remaining." % self.number_of_pirates)
            print("You have %s cannons and your ship health is %s" % (self.game.cannons, self.game.ship_health))
            print("")
            attack_input = input("What do you wish to do? R)un or F)ight? ")
            if attack_input.upper() == 'R':
                if self.run():                       # True if you got away
                    FightingPirates = False
            if attack_input.upper() == 'F':
                if self.fight():                     # True if fight is over
                    FightingPirates = False
            self.ship_damage()                        
            print("Press any key to continue....")
    
    def ship_damage(self):
        damage = random.randint(0,self.number_of_pirates *2)
        self.game.ship_health -= damage
        if damage <= 0:
            print("Ship Destroyed")
    
    def fight(self):
        fight_strength = 1 if self.game.cannons == 0 else self.game.cannons + 1
        attack = random.randint(0, fight_strength + 1)
        pirates_killed = attack if self.number_of_pirates >= attack else self.number_of_pirates
        self.number_of_pirates -= pirates_killed
        if self.number_of_pirates <= 0:
            return True
        else:
            return False
    
    def run(self):
        print("You try to run")
        result = random.randint(0,100)
        if result <= self.chance_for_escape:
            print("You escaped from the pirates!!")
            return True
        else:
            print("You didn't get away from the Pirates!!")
            return False
        input("Press any key to continue....")