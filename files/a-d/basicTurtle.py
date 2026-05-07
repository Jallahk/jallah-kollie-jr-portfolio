"""
Turtle Basics
"""
import turtle

t = turtle.Turtle()
win=turtle.Screen()
for i in range(20):
    
    t.color("red")
    t.forward(20)
    t.right(100)
    t.forward(50)
    t.left(80)
    t.color("blue")
    t.backward(30)
    t.left(90)
    t.color('green')
    t.forward(120)
t.forward(100)
win.exitonclick()