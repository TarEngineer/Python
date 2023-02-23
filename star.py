import turtle

def draw_star(turtle, size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

t = turtle.Turtle()
t.penup()
t.goto(-100,100)
t.pendown()

for i in range(5):
    draw_star(t, 200)
    t.penup()
    t.forward(350)
    t.pendown()

turtle.done()
