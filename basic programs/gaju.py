from turtle import *
bgcolor("black")
speed(0)
hideturtle()
for i in range(70):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    color("green")
    circle(i*0.6)

    right(10)
    forward(3)
done()
