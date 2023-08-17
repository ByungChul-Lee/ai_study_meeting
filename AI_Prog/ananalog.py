import turtle
import time

turtle.mode("logo")

ws = turtle.Screen()
ws.bgcolor("orange")
ws.setup(width=600, height=600)
ws.title("Analog Clock")
ws.tracer(0)


t1 = turtle.Turtle()
t1.hideturtle()
t1.speed(0)

t = turtle.Turtle()
t.shape("circle")
t.hideturtle()
t.speed(0)

tm = turtle.Turtle()
tm.pensize(3)
tm.hideturtle()
tm.speed(0)

th = turtle.Turtle()
th.pensize(6)
th.hideturtle()
th.speed(0)

def draw_clock(tur):
    
    for i in range(12):
        tur.penup()
        tur.goto(0,0)
        tur.setheading(i*30)
        tur.forward(240)
        tur.right(90)
        tur.pendown()
        tur.circle(10)
        
draw_clock(t1)

while True:
    sec =  int(time.strftime("%S"))
    min = int(int(time.strftime("%M"))*6 + sec // 10.0)
    hour = int(int(time.strftime("%I"))*30 + int(time.strftime("%M")) // 2.0)
    
    t.setheading(sec*6)
    tm.setheading(min)
    th.setheading(hour)
    
    t.forward(200)
    tm.forward(150)
    th.forward(100)
    
    t.penup()
    tm.penup()
    th.penup()
    
    ws.update()
    time.sleep(1)
    t.clear()
    tm.clear()
    th.clear()
    
    t.goto(0,0)
    t.pendown()
    
    
    tm.goto(0,0)
    tm.pendown()
    
 
    th.goto(0,0)
    th.pendown()
        
        
        