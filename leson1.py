from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

begin_fill()
forward(70)
color("yellow")
left(90)
forward(120)     #height of the door
right(90)
forward (60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("Purple")    #we want to draw a window
left(30)
forward(70)
left(90)
penup()
goto(70, 130)
pendown()

color("blue")

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(130, 130)
pendown()


forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


color("green")
penup()
goto(200,0)
pendown()
left(90)
forward(500)     #we want to draw a grass
begin_fill
penup()
goto(200, 0)
left(180)
pendown()
forward(700)






exitonclick()