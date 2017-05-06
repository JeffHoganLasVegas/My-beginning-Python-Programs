import turtle

def draw_polygon(jeff_turtle):
    for i in range(1,9):
        jeff_turtle.forward(45)
        jeff_turtle.left(45)

def draw_triangle(jill_turtle):
    for i in range(1,4):
        jill_turtle.forward(100)
        jill_turtle.left(120)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Creat the turtle jeff_turtle to draw a polygon
    jeff_turtle=turtle.Turtle()
    jeff_turtle.shape("turtle")
    jeff_turtle.color("yellow")
    jeff_turtle.speed(2)
    draw_polygon(jeff_turtle)


    #Creat the turtle Jill_turtle to draw a triangle
    jill_turtle=turtle.Turtle()
    jill_turtle.shape("turtle")
    jill_turtle.color("green")
    jill_turtle.speed(2)
    draw_triangle(jill_turtle)


    #Creat the turtle Jack_turtle to draw a circle
    jack_turtle = turtle.Turtle()
    jack_turtle.shape("turtle")
    jack_turtle.color("black")
    jack_turtle.circle(100)


    window.exitonclick()


draw_art()
