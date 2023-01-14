from turtle import *
left(90)
for i in range(7):
    forward(150)
    right(120)
penup()
for x in range(1, 11):
    for y in range(1, 11):
        goto(x*15, y*15)
        dot(5)
done()
