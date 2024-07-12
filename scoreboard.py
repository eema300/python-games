from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.score = 0
    with open('high_score.txt', mode='r') as record:
      self.high_score = int(record.read())
    self.color('white')
    self.penup()

  def create_scoreboard(self):
    with open('high_score.txt', mode='r') as record:
      self.high_score = int(record.read())
    self.clear()
    self.goto(x=0, y=260)
    self.write(arg=f"score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)
    self.penup()

  def add_point(self):
    self.goto(x=0, y=260)
    self.score += 1
    self.clear()
    self.write(arg=f"score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def reset_score(self):
    self.goto(x=0, y=260)
    if self.score > self.high_score:
      self.high_score = self.score
    self.score = 0
    self.clear()
    with open('high_score.txt', mode='w') as record:
      record.write(str(self.high_score))
    self.write(arg=f"score: {self.score} high score: {self.high_score}", align=ALIGNMENT, font=FONT)

  # *** DEPRECATED *** use reset() instead
  def game_over(self):
    pass

  def start_game(self):
    self.goto(0, 0)
    self.write(arg='press space to start', align=ALIGNMENT, font=FONT)