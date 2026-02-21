from turtle import *
pendown()
for i in range(4):
    forward(100)
    right(90)
    forward(200)
    right(90)

penup()
for x in range(0, 200, 20):
    for y in range(0, 200, 20):
        goto(x, -y)
        dot(5)
done()