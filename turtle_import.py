from turtle import *

zike = Turtle()
rose = Turtle()
eola = Turtle()

zike.color("purple")

rose.color("red")

eola.color("green")
all_t = [zike, rose, eola]

for t in all_t:
    t.shape("turtle")


for i in range(69):
    zike.forward(50)
    zike.right(99)

    rose.forward(61)
    rose.left(68)

    eola.forward(92)
    eola.right(84)

    
speed(10)
