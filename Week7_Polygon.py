import turtle
t = turtle

sides = int(input('Enter the Number of sides for your polygon: '))
side_length = int(input('Enter the length of the sides for your polygon: '))

def draw_polygon(side_length, sides):
    for i in range(0, sides):
        t.forward(side_length)
        angle = 360 / sides
        t.right(angle)
    t.forward(side_length)
    turtle.done()
draw_polygon(side_length, sides)
