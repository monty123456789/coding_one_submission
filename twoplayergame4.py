from turtle import Turtle, Screen
import turtle
import random


#Setting up the interface
wn = Screen()
wn.title("Monty's Python Game")
wn.setup(width=800, height=800)
wn.bgcolor('green')
#allows the game to move at a smooth speed
wn.tracer(0, 0)


#creating the food the player will move over to score points, 
# by creating the food outside of the Snake class, it means each player will be chasing the same food, making the game more two-player orientated and more competitive.    
food = turtle.Turtle()
food.penup()
food.goto(60,60)
food.speed(0)
food.shape('circle')
food.color('white')
food.fillcolor('black')

#Creating the class 'Snake', this is the class from which the two player instances will be made from
class Snake:
    
    #the parameters in __init__ are the parameters that allow the player instances to be called, e.g. 'color' allows the instances to be called with different colors so the players know who is who
    def __init__(self, goto, color, player, setx, sety):
      
        self.sc = Screen()

        #setting up the 'head' of the player, this is the square the player will move. 
        self.head = Turtle()
        self.head.color(color)
        self.head.fillcolor('white')
        self.head.shapesize(outline=5)
        self.head.shape('square')
        self.head.penup()
        self.head.speed(0)
        self.head.goto(goto)
        self.head.direction = 'stop'
        
        
        #setting up the point system and player graphics
        self.score = 0
        self.player = player
        self.pen = Turtle()
        self.pen.color('black')
        self.color = color

        self.pen.speed(0)
        self.pen.shapesize(outline=10)
        self.pen.fillcolor('white')
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(setx, sety)
        self.pen.write('Player {} ({}) Score: {}'.format(self.player, self.color, self.score), align='center', font=('courier', 24, 'normal'))

        #This will be increased every time a player moves over food to increase the speed, or decrease if they hit a border. 
        self.di = 7
        
    # assigning keys
    def move(self, left_key, right_key, up_key, down_key):
        self.sc.listen()
        self.sc.onkey(self.up, up_key)
        self.sc.onkey(self.down, down_key)
        self.sc.onkey(self.left, left_key)
        self.sc.onkey(self.right, right_key)
     
     #creating the turn functions
    def turn(self):
    
        if self.head.direction == 'left':
            l = self.head.xcor()
            self.head.setx(l - self.di)

        if self.head.direction == 'right':
            r = self.head.xcor()
            self.head.setx(r + self.di)

        if self.head.direction == 'up':
            u = self.head.ycor()
            self.head.sety(u + self.di)

        if self.head.direction == 'down':
            d = self.head.ycor()
            self.head.sety(d - self.di)


    def left(self):
        self.head.direction = 'left'

    def right(self):
        self.head.direction = 'right'

    def up(self):
        self.head.direction = 'up'

    def down(self):
        self.head.direction = 'down'

    #This function resets the player position and decreases the speed if they get too close the edge of the screen, unless their speed is already less than 7.
    # It also decreases the player score by 10 every time they collide with the edge of the screen, unless they already have zero points, in which case their score remains the same.
    #This means that a player's speed will always increase or decrease at the same level as their points.
   
    def border_c(self):
        if self.head.xcor()>390 or self.head.xcor()<-390 or self.head.ycor()>390 or self.head.ycor()<-390:
            
            self.head.goto(0,0)
            if self.di > 7:
                self.di -= 1
            elif self.di < 7:
                pass
            if self.score >= 10:
                self.score -= 10
                self.pen.clear()
                self.pen.write('Player {} ({}) Score: {}'.format(self.player, self.color, self.score), align='center', font=('courier', 24, 'normal'))

            elif self.score < 10:
                pass
    
    #This function increases the score and speed if the player moves over food, and moves the food to a new position. 
    def scores(self):
        self.random = random
        if self.head.distance(food) < 20:
            
            self.di += 1
            self.score += 10 
        
            self.pen.clear()
            self.pen.write('Player {} ({}) Score: {}'.format(self.player, self.color, self.score), align='center', font=('courier', 24, 'normal'))
            
            y = self.random.randint(-390, 390)
            x = self.random.randint(-390, 390)
            food.goto(x,y)

           
            
            #This ends the game when a player has a score of 100, and announces the winner. 
            if self.score > 95:
                self.pen.goto(0,0)
                self.pen.color('black')
                self.pen.fillcolor('black')
                self.pen.shapesize(outline=20)
                self.pen.write('Player {}  is the winner!'.format(self.player), align='center', font=('courier', 40, 'bold'))
                wn.mainloop()
          
#Creates two player instances
player1 = Snake((-30,30), 'red', '1', -200, 360)
player2 = Snake((30,30), 'blue', '2', 200, 360)

#creates the game loop that calls the functions on the instances. 
while True:
    player1.move('a', 'd', 'w', 's')
    player1.border_c()
    player1.turn()
    player1.scores()

    player2.move('j', 'l', 'i', 'k')
    player2.turn()
    player2.border_c()
    player2.scores()

    wn.update()

wn.mainloop()
