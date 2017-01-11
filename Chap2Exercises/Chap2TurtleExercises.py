import turtle

""" Chapter 2 Turtle Exercises """
'''
# Exercise 2.23: Draw four circles in the center of the screen, prompt the users for the radius
radius = abs(eval(input("Enter the radius for all four circles: ")))
turtle.up()
turtle.goto(0,0)
turtle.goto(-radius,radius)
turtle.color('#006600')
turtle.pd()
turtle.circle(radius)
turtle.penup()
turtle.goto(radius,radius)
turtle.pendown()
turtle.color('red')
turtle.circle(radius)
turtle.up()
turtle.goto(radius,-radius)
turtle.pd()
turtle.color('blue')
turtle.circle(radius)
turtle.penup()
turtle.goto(-radius,-radius)
turtle.pd()
turtle.color('purple')
turtle.circle(radius)
turtle.reset()
'''

#Exercise 2.24 Draw a polygon

turtle.color('purple')
turtle.penup()
turtle.goto(0,0)
turtle.goto(40, -69.28)
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80,0)
turtle.goto(40, -69.28)


turtle.color('purple')
turtle.penup()
turtle.goto(0,0)
turtle.left(30)
turtle.goto(40, -69.28)
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80,0)
turtle.goto(40, -69.28)


#turtle.reset()

