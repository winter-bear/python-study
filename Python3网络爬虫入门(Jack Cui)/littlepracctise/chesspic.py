#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
i = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a !=b)and(b !=c)and(c !=a):
                print(a,b,c)
                i = i+1

print("there is %d choices of num groups" %i)

import sys
for i in range(8):
        for j in range(8):
                if (i + j) % 2 != 0:
                        print(chr(219),end='')
                        print(chr(219),end='')
                else:
                        print('  ',end='')
        print('\n',end='')
'''
import turtle
def drawSquare():
    turtle.pendown()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.penup()
turtle.speed(30)
turtle.penup()
off = True
for y in range(-40, 30 + 1, 10):
    for x in range(-40, 30 + 1, 10):
        if off:
            turtle.goto(x, y)
            turtle.begin_fill()
            turtle.color("black")
            drawSquare()
            turtle.end_fill()
            turtle.penup()
        else:
            turtle.goto(x, y)
            drawSquare()
        off = bool(int(off) - 1)
    off = bool(int(off) - 1)
turtle.hideturtle()
turtle.done()   
