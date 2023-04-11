from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
ball = Ball()
score = ScoreBoard()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    # detect collision from wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detect collision from right paddle
    if ball.xcor() > 340 and ball.distance(right_paddle) < 50 or ball.xcor() < -340 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
        # detect collision from right paddle
    # collision from right paddle wall
    if ball.xcor() > 390:
        score.l_point()
        ball.refactor()
    # collision from left paddle wall
    if ball.xcor() < -390:
        score.r_point()
        ball.refactor()

screen.exitonclick()
