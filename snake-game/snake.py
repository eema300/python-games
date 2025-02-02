from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
WALL_MIN = -300
WALL_MAX = 300

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def add_segment(self, position):
    new_segment = Turtle('square')
    new_segment.color('green')
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)
    self.tail = self.segments[-1]

  def create_snake(self):
    for position in STARTING_POSITIONS:
      self.add_segment(position)

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
     
  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)

  def hit_wall(self):
    if self.head.xcor() >= WALL_MAX or self.head.xcor() <= WALL_MIN or self.head.ycor() >= WALL_MAX or self.head.ycor() <= WALL_MIN:
      return True

  def extend(self):
    position = self.tail.pos()
    self.add_segment(position)

  def hit_self(self):
    for segment in self.segments[1:]:
      if self.head.distance(segment) < 10:
        return True

  def reset_player(self):
    for segment in self.segments:
      segment.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
    self.tail = self.segments[-1]
    
