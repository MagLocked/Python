import turtle
import random as rd
import math
rosa = "#FF5C77"
turkis = "#4DD091"
gul = "#FFEC59"
oransje = "#FFA23A"
gra = "#74737A"

turtle.bgcolor("#FF5C77")
t = turtle.Turtle()
t.pen(speed=1000, pensize = 5)
t.shape("circle")
t.color(gul, oransje)
t.penup()
t.goto(-250, -260)

# tegner oddetallsradene på brettet
y = -260
for i in range(0, 3):
    for i in range(0,5):
        t.begin_fill()
        for p in range(0,4):
            t.fd(100)
            t.lt(90)
        t.end_fill()
        t.fd(100)
        if i%2 != 0:
            t.color(gul, oransje)
        else:
            t.color(oransje, gul)
    t.color(gul, oransje)
    y +=200
    t.goto(-250, y)
# tegner partallsradene på brettet
t.goto(-250, -160)
t.color(oransje, gul)
y = -160
for i in range(0, 2):
    for i in range(0,5):
        t.begin_fill()
        for p in range(0,4):
            t.fd(100)
            t.lt(90)
        t.end_fill()
        t.fd(100)
        if i%2 == 0:
            t.color(gul, oransje)
        else:
            t.color(oransje, gul)
    t.color(oransje, gul)
    y +=200
    t.goto(-250, y)
  
# tegner ramme
t.goto(-250, -260)   
t.pendown()     
t.color(gra)
t.pensize(10)
for i in range(4):
    t.fd(500)
    t.lt(90)

# tegner stiger
stiger = [
    [0, 190, 200, -10],
    [100, -210, 0, 90],
    [-200, -210, -100, -110],
    [-200, -110, -200, 190],
    [-100, -10, 0, -210]
    ]
t.penup()
t.pensize(5)
t.color(gra, rosa)
t.shapesize(2,2,2)

def tegnStige(l):
    t.goto(l[0], l[1])
    t.pendown()
    t.goto(l[2], l[3])
    t.stamp()
    t.penup()

for i in stiger:
    tegnStige(i)



p1=turtle.Turtle()
p1.penup()
p1.shape("turtle")
p1.shapesize(2,2,2)
p1.goto(-300,-210)
p2=p1.clone()
p2.shape("circle")

def flytt(x):
    upL=[-110,90]
    upR=[-210,-10]
    terning=rd.randint(1,4)
    print(terning)
    moveP1=terning*100
    print(moveP1)
    while True:
        yP=round(x.ycor(),0)
        xP=round(x.xcor(),0)
        moveP1=round(moveP1, 0)
        print("xcor=",x.xcor())
        print("ycor=",x.ycor())
        if xP==200 and yP==190:
            print("P1 VINNER!")
            break
        if moveP1<=0:
            break
        else:
            for i in upR:
                if xP==200 and yP==i:
                    x.lt(90)
                    x.fd(100)
                    moveP1-=100
                    x.lt(90)
            for i in upL:
                if xP==-200 and yP==i:
                    x.rt(90)
                    x.fd(100)
                    moveP1-=100
                    x.rt(90)
            else:
                x.fd(100)
                moveP1-=100
        print("antall",moveP1)
    for i in stiger:
        if xP==i[0] and yP==i[1]:
            x.goto(i[2],i[3])
            if abs(i[1]-i[3])==100 or abs(i[1]-i[3])==300:
                x.lt(180)
    return
while True:
    yP2=round(p2.ycor(),0)
    xP2=round(p2.xcor(),0)
    #
    yP1=round(p1.ycor(),0)
    xP1=round(p1.xcor(),0)
    tur=input("Trykk ENTER for å gå videre...")
    if xP1==200 and yP1==190:
        p1.goto(0,0)
        p1.shapesize(4,4,4)
        p1.color("yellow", "orange")
        break
    if xP2==200 and yP2==190:
        p2.goto(0,0)
        p2.shapesize(4,4,4)
        p2.color("yellow", "orange")
        break
    else:
        flytt(p1)
        flytt(p2)
        
turtle.done()
try:
    turtle.bye()
except turtle.Terminator:
    pass