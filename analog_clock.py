import turtle
import time


wn = turtle.Screen()
#changing background color
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Simple Analog Clock by Szymoo")
# turns off animation
wn.tracer(0)

# Creating our wee turtle
pen = turtle.Turtle()
#I wanna hide it, still wanna drawing using it, just dont see it
pen.hideturtle()
# Animation speed, it will draw as fast as it can
pen.speed(0)
#Width of the pen
pen.pensize(3)

def draw_clock(h, m, s, pen):

    #Draw clock face
    pen.up()
    pen.goto(0, 210)
    #setheading 0 - pointing east, 90 - pointin north 180 - west, 270- south
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    #210 - radius of the circle
    pen.circle(210)

    # Draw the lines for the hours
    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    # Draw the hour hand

    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    angle = ( h /12 ) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # Draw the minute hand

    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = ( m / 60 ) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # Draw the second hand

    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = ( s / 60 ) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

while True:
    
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%s"))

    draw_clock(h, m, s, pen)
    #because we used wn.tracer() before, it draws in computer's memory. When we do wn.update() it will upadate in the screen
    wn.update()
    time.sleep(1)

    pen.clear()









wn.mainloop()
