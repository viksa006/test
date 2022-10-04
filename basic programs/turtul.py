from turtle import *
bgcolor("black")
speed(0)
speed(0)
speed(0)
hideturtle()
for i in range(150):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    color("white")
    circle(i*0.2)

    right(20)
    forward(3)
done()
