import turtle
t = turtle
from random import seed
from random import randint

iterations1 = int(input('Enter the number of iterations of your random walker: '))
length1 = int(input('Enter the length of the lines of your random walker: '))


def draw_random(length1, iterations1):

    for i in range(0, iterations1):
        
        for i in range(0, iterations1):
            value = randint(0,3)

            if value == 0:
                t.forward(length1)
            elif value == 1:
                t.right(90)
                t.forward(length1)
            elif value == 2:
                t.left(90)
                t.forward(length1)
            elif value == 3:
                t.backward(length1)
            


        turtle.done()

draw_random(length1, iterations1)