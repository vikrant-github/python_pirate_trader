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
            print("There are %s pirates remaining." % self.number_of_pirates)
            print("You have %s cannons and your ship health is %s" % (self.game.cannons, self.game.ship_health))
            print("")
            attack_input = input("What do you wish to do? R)un or F)ight? ")
            if attack_input.upper() == 'R':
                if self.run():
                    FightingPirates = False
            if attack_input.upper() == 'F':
                self.fight()
            print("Press any key to continue....")
    def fight(self):
        pass
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