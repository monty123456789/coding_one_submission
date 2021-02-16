###number of sides
##number of dice
#number of rolls

from random import randint



class DiceRoller:
    
    def __init__(self, quantity, sides, roles):
        self.sides = sides
        self.quantity = quantity
        self.roles = roles

    def roledice(self):
        for j in range(1, self.quantity + 1):
            for x in range(1, self.roles + 1):
                result = randint(1, self.sides) 

                print('dice: {} role: {} is: {}'.format(j, x, result) )

           








