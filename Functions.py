from random import randint
from myShape import *

def ring(t,side):
    for times in range(side):
        t.begin_fill()
        red=randint(0,255)
        green=randint(0,255)
        blue=randint(0,255)
        t.color(red,green,blue)
        square(t,100)
        t.left(6)
        t.end_fill()

def background(t,side):
    for times in range(side):
        t.begin_fill()
        square(t,500)
        t.color(180,0,0)
        move(t,0,0)
        polygon(t,100,1)
        t.left(6)
        t.end_fill()

def hole(t,distance,side):
    angle=360/side
    for times in range(side):
        t.begin_fill()
        t.color(180,0,0)
        move(t,0,0)
        t.circle(distance)
        t.left(angle)
        t.end_fill()
