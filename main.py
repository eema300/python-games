import time
from turtle import Screen, Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

STARTING_POSITION_R = (380, 220)
STARTING_POSITION_L = (-380, 0)

# setup screen
win = Screen()
win.bgcolor('black')
win.title('pong')
win.setup(width=800, height=600)
win.tracer(0)
line = Turtle()
line.hideturtle()
line.color('white')
line.penup()
line.goto(0, -300)
line.pendown()
line.goto(0, 300)

# create gameboard, paddles, ball, show on screen
scoreboard = ScoreBoard()
paddle_R = Paddle(STARTING_POSITION_R)
paddle_L = Paddle(STARTING_POSITION_L)
paddles = [paddle_L, paddle_R]
ball = Ball()
win.update()

# allow movement
win.listen()
win.onkey(fun=paddle_R.up, key='Up')
win.onkey(fun=paddle_R.down, key='Down')
win.onkey(fun=paddle_L.up, key='w')
win.onkey(fun=paddle_L.down, key='s')

# gameplay
game_is_on = True
while(game_is_on):
  time.sleep(ball.move_speed)
  win.update()
  ball.move(paddles)
  if ball.cross_boundary():
    ball.reset_pos()
    scoreboard.add_point(ball.loser)
  game_is_on = scoreboard.check_winner()
scoreboard.disp_winner()


win.mainloop()