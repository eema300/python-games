from turtle import Turtle

MOVE_DISTANCE = 10
TOP_WALL = 280
BOTTOM_WALL = -280
PADDLE_HIT_BOX = 50
RIGHT_PADDLE_BORDER = 360
LEFT_PADDLE_BORDER = -360

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('white')
    self.speed('fastest')
    self.penup()
    self.x_move = MOVE_DISTANCE
    self.y_move = MOVE_DISTANCE
    self.loser = None
    self.move_speed = 0.1

  def bounce_y(self):
    self.y_move = -self.y_move

  def bounce_x(self):
    self.x_move = -self.x_move

  def hit_wall(self):
    if self.ycor() >= TOP_WALL or self.ycor() <= BOTTOM_WALL:
      return True

  def hit_paddle(self, paddles):
    if (self.xcor() == LEFT_PADDLE_BORDER or self.xcor() == RIGHT_PADDLE_BORDER) and (self.distance(paddles[0]) < PADDLE_HIT_BOX or self.distance(paddles[1]) < PADDLE_HIT_BOX):
      self.move_speed *= 0.9
      print(self.move_speed)
      return True

  def cross_boundary(self):
    if self.xcor() >= 400 or self.xcor() <= -400:
      self.loser = 'R' if self.xcor() >= 400 else 'L'
      return True

  def reset_pos(self):
    self.goto(0, 0)
    self.bounce_x()
  
  def move(self, paddles):
    if self.hit_wall():
      self.bounce_y()
    if self.hit_paddle(paddles):
      self.bounce_x()
    self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)