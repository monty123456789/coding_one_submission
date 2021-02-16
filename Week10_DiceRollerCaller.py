from Week10_diceroller import DiceRoller



sides1 = int(input('How many sides do your dice have? : '))
quantity1 = int(input('How many dice do you have? : '))
rolls1 = int(input('How many times would you like to role your dice? : '))

roll1 = DiceRoller(quantity1, sides1, rolls1)
roll1.roledice
print(roll1.roledice())