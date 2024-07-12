from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score_L = 0
    self.score_R = 0
    self.winner = None
    self.hideturtle()
    self.color('white')
    self.penup()
    self.goto(0, 240)
    self.write(arg=f"{self.score_L}    {self.score_R}", align=ALIGNMENT, font=FONT)
    
  def add_point(self, loser):
    if loser == 'R':
      self.score_L += 1
    elif loser == 'L':
      self.score_R += 1
    self.clear()
    self.write(arg=f"{self.score_L}    {self.score_R}", align=ALIGNMENT, font=FONT)

  def check_winner(self):
    if self.score_L == 10 or self.score_R == 10:
      self.winner = 'Left' if self.score_L == 10 else 'Right'
      return False
    return True

  def disp_winner(self):
    if self.winner is not None:
      self.goto(0, 0)
      self.write(arg=f"{self.winner} Player Wins!", align=ALIGNMENT, font=FONT)