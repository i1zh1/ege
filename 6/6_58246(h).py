from turtle import *
speed(10)
penup()
goto(0, -400)
pendown()
right(180)
forward(40)
right(90)
forward(800)
right(90)
forward(40)
right(180)
for i in range(4):
    circle(100, -180)
    right(180)
penup()
for x in range(-100, 140, 20):
    for y in range(-500, 500, 20):
        goto(x, y)
        dot(5)

done()