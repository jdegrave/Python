import turtle

# Python Chapter 1 Turtle Exercises
# Contains code for exercises 1.12 - 1.21
# Author: Jodi A. DeGrave
# Date:   2/8/2016

#Excercise 1.12 Draw a square
turtle.showturtle()
turtle.delay(20)
turtle.color('red')
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left (90)
turtle.forward(200)
turtle.penup()
turtle.goto(-100, 0)
turtle.color('blue')
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.reset()          # Clear turtle canvas and return pointer to position (0,0) for next exercise

# Exercise 1.13 Draw a cross
turtle.penup()
turtle.goto(0,100)
turtle.color('green')
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.penup()
turtle.goto(-100,0)
turtle.left(90)
turtle.pendown()
turtle.forward(200)
turtle.reset()

#Exercise 1.14 Draw a triangle
turtle.color('purple')
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(140)
turtle.right(135)
turtle.forward(100)
turtle.reset()

#Exercise 1.15 Draw 2 triangles in the shape of an hour glass
turtle.color('#ff00ff')
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(140)
turtle.right(135)
turtle.forward(200)
turtle.left(135)
turtle.forward(140)
turtle.left(135)
turtle.forward(100)
turtle.reset()

#Exercise 1.16 draw four circles in the center of the screen

turtle.up()
turtle.goto(-75,75)
turtle.pd()
turtle.color('#006600')
turtle.circle(75)
turtle.penup()
turtle.goto(75,75)
turtle.pendown()
turtle.color('red')
turtle.circle(75)
turtle.up()
turtle.goto(75,-75)
turtle.pd()
turtle.color('blue')
turtle.circle(75)
turtle.penup()
turtle.goto(-75,-75)
turtle.pd()
turtle.color('purple')
turtle.circle(75)
turtle.reset()

#Exercise 1.17 Draw a line between 2 coordiantes and display those coordinates
turtle.penup()
turtle.color('blue')
turtle.goto(-39,49)
turtle.pendown()
turtle.write('-39,49')
turtle.goto(50,-50)
turtle.write('50,-50')
turtle.hideturtle()
turtle.reset()


#Exercise 1.18 Draw a star (hint: inner angle of each point is 36 degrees

turtle.showturtle()
turtle.penup()
turtle.goto(-100,100)
turtle.pendown()
turtle.color('red')
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.reset()

#Exercise 1.19 Draw a polygon
turtle.penup()
turtle.goto(40, -69.28)
turtle.color('purple')
turtle.pendown()
turtle.goto(-40, -69.28)
turtle.goto(-80, -9.8)
turtle.goto(-40, 69)
turtle.goto(40, 69)
turtle.goto(80,0)
turtle.goto(40, -69.28)
turtle.reset()



#Exercise 1.20 Draw a rectanguloid
turtle.penup()
turtle.goto(-100,0)
turtle.pd()
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.left(45)
turtle.forward(50)
turtle.left(45)
turtle.forward(200)
turtle.left(135)
turtle.forward(50)
turtle.penup()
turtle.goto(100,100)
turtle.right(175)
turtle.pendown()
turtle.forward(50)
turtle.right(50)
turtle.forward(105)
turtle.penup()
turtle.goto(-100,100)
turtle.right(-45)
turtle.pendown()
turtle.forward(50)
turtle.right(45)
turtle.forward(100)
turtle.penup()
turtle.goto(-65,65)
turtle.right(-90)
turtle.pendown()
turtle.forward(202)
turtle.ht()
turtle.reset()

#Exercise 1.12 Draw a clock that display 9:15:00
#Draw the numbers first
turtle.penup()
turtle.goto(100,0)
turtle.pd()
turtle.write('3')
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.write('6')
turtle.up()
turtle.goto(-100,0)
turtle.down()
turtle.write('9')
turtle.up()
turtle.goto(0, 100)
turtle.down()
turtle.write('12')
turtle.up()

#Draw the circle. Make the radius a little longer so the circle encloses the numbers
turtle.goto(0,-110)
turtle.down()
turtle.circle(115)
turtle.penup()

#Display the time below the clock face
turtle.goto(-10,-140)
turtle.pendown()
turtle.write('9:15:00')

#Draw the hour, minute, and second hands
turtle.penup()
turtle.goto(0,0)
turtle.down()
turtle.color('red')
turtle.goto(0,100)
turtle.up()
turtle.goto(100,0)
turtle.color('black')
turtle.down()
turtle.goto(-100, 0)
turtle.left(180)  #Use the turtle as the head of the hour head by pointing it to 9 o'clock

turtle.done()