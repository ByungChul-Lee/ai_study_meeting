from turtle import *
import turtle
import time



ws = turtle.Screen()
ws.bgcolor("black")
ws.setup(width=600, height=600)
ws.title("Analog Clock")
#ws.tracer(0)



tur = turtle.Turtle()
tur.hideturtle()
tur.speed(0)
tur.pensize(3)



def draw_second(hour, min, second):
    tur.color("red")
    tur.up()
    tur.goto(0, 0)
    tur.setheading(90)
    for _ in range(12):
        tur.fd(190)
      
        
        tur.pendown()
        tur.circle(20)  #fd(20)
        
        tur.penup()
        tur.goto(0, 0)
        tur.rt(30)



    tur.color("blue")
    tur.home()
    tur.setheading(90)
    tur.rt(min*6)
    tur.pendown()
    tur.fd(140)



    tur.color("orange")
    tur.home()
    tur.setheading(90)
    tur.rt(second*6)
    tur.pendown()
    tur.fd(120)

    

while True:    

    hour = int(time.strftime("%I"))
    min = int(time.strftime("%M"))
    second = int(time.strftime("%S"))
    print(hour,":",min,":",second)

    ws.update()
    time.sleep(1)
    tur.clear()

    draw_second(hour, min, second)