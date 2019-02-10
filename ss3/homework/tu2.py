import turtle
from turtle import *
t=turtle.Turtle()
for i in ["red","blue", 'brown', 'yellow', 'grey']:
    t.color(i)
    t.begin_fill()
    for j in range(2):
        t.forward(40)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.forward(40)
    t.end_fill()
turtle.done()
