from turtle import *

pendown()
for i in range(7):
    forward(150)
    right(120)
penup()
for x in range(0, 200, 15):
    for y in range(0, 200, 15):
        goto(x,-y)
        dot(5,)
done()