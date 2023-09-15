 #"help", "copyright", "credits" or "license" for more information.
import turtle
import time
list1 = ("red","green","blue","yellow","purple","orange")
s = turtle.Turtle()
s.hideturtle()
def key_test():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(4)
    t.rt(90)
    t.color("black","skyblue")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.rt(90)
    t.pensize(7)
    t.forward(10)
    t.pensize(4)
    t.rt(90)
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.penup()
    t.goto(120,1)
    t.pendown()
    t.rt(45)
    t.forward(110)
    t.penup()
    t.goto(-130,-5)
    t.pendown()
    t.forward(130)
    
key_test()
for j in range(5):
    
    for i in list1:
        s = turtle.bgcolor(i)
        time.sleep(0.2)
    