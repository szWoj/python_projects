import turtle

window = turtle.Screen()
window.title("Pong by Szymon")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0) # stops the window from updating
# Score
score_left = 0
score_right = 0


## Paddle A
paddle_left = turtle.Turtle()
paddle_left.speed(0) # speed of looping, not of paddle moving
paddle_left.shape("square")
paddle_left.color("white")
paddle_left.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_left.penup()
paddle_left.goto(-385, 0)



## Padle B
paddle_right = turtle.Turtle()
paddle_right.speed(0) # speed of looping, not of paddle moving
paddle_right.shape("square")
paddle_right.color("white")
paddle_right.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_right.penup()
paddle_right.goto(375, 0)


## Ball
ball = turtle.Turtle()
ball.speed(0) # speed of looping, not of paddle moving
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # every loop, it moves 2 pixels on x and 2 pixels on y (so diagonal)
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))



# Function
def paddle_left_up():
    y = paddle_left.ycor()
    y += 20
    paddle_left.sety(y)

def paddle_left_down():
    y = paddle_left.ycor()
    y -= 20
    paddle_left.sety(y)

def paddle_right_up():
    y = paddle_right.ycor()
    y += 20
    paddle_right.sety(y)

def paddle_right_down():
    y = paddle_right.ycor()
    y -= 20
    paddle_right.sety(y)



# Keyboard binding
window.listen()
window.onkeypress(paddle_left_up, "w")
window.onkeypress(paddle_left_down, "s")
window.onkeypress(paddle_right_up, "Up")
window.onkeypress(paddle_right_down, "Down")

#main game loop

while True:
    window.update() # every time the loop runs, screen gets updated

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_right += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        

    elif ball.xcor() < -390:
        score_left += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_left, score_right), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
        score_left += 1

    # Paddle and ball collisions
    if ball.xcor() > 365 and ball.ycor() < paddle_right.ycor() + 40 and ball.ycor() > paddle_right.ycor() - 40:
        ball.setx(365)
        ball.dx *= -1

    if ball.xcor() < - 375 and ball.ycor() < paddle_left.ycor() + 40 and ball.ycor() > paddle_left.ycor() - 40:
        ball.setx(-375)
        ball.dx *= -1
