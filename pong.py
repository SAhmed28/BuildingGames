# Simple Pong game in Python3

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by Ryan")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)        # stops the window from updating, this will speed up our game

# Score
score_a = 0
score_b = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')    # it will create a 20px by 20px square
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    #this will stretch width 5 times
paddle_a.penup()    # we don't need to draw anything
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')    # it will create a 20px by 20px square
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    #this will stretch width 5 times
paddle_b.penup()    # we don't need to draw anything
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')    # it will create a 20px by 20px square
ball.color("white")
ball.penup()    # we don't need to draw anything
ball.goto(0,0)
# Ball moving
ball.dx = 0.2
ball.dy = - 0.2

# Score Pen
pen = turtle.Turtle()
pen.speed(0)   # animation speed, not the moving speed!
pen.color("Green")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0       Player B: 0",align="center", font=("Courier",20,"bold"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main game loop
while True:
    wn.update()

    # Move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   # move the ball opposite diretion
        # winsound.PlaySound('game-ball-bounce2.wav', winsound.SND_ASYNC)

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # winsound.PlaySound('game-ball-bounce2.wav', winsound.SND_ASYNC)

    # Left and Right
    if ball.xcor() > 390:   # Right side hit
        ball.goto(0,0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "bold"))
        winsound.PlaySound('game-ball-bounce3.wav', winsound.SND_ASYNC)

    elif ball.xcor() < -390:   # Left side hit
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center",font=("Courier", 20, "bold"))
        winsound.PlaySound('game-ball-bounce3.wav', winsound.SND_ASYNC)


    # Paddle and ball collisions
    # if ball is touching the paddle edge, and ball is between the paddle height
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+60 and ball.ycor() > paddle_b.ycor()-60):
        ball.setx(340)   # after touching surface, back a little bit
        ball.dx *= -1      # go to opposite direction
        winsound.PlaySound('game-ball-bounce1.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+60 and ball.ycor() > paddle_a.ycor()-60):
        ball.setx(-340)   # after touching surface, back a little bit
        ball.dx *= -1      # go to opposite direction
        winsound.PlaySound('game-ball-bounce1.wav', winsound.SND_ASYNC)


