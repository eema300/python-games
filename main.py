import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake


# set up screen
win = Screen()
win.setup(width=600, height=600)
win.bgcolor('black')
win.title('snake game')
win.tracer(0)

# initialize object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
scoreboard.start_game()

# game play logic
def play_game():
  scoreboard.create_scoreboard()
  game_is_on = True
  while (game_is_on):
    win.update()
    time.sleep(0.1)
    snake.move()
    
    # detect wall
    if snake.hit_wall() or snake.hit_self():
      scoreboard.reset_score()
      snake.reset_player()
      game_is_on = False
      scoreboard.start_game()
      
    # detect food
    if food.distance(snake.head) < 15:
      food.appear()
      scoreboard.add_point()
      snake.extend()
  

win.listen()
win.onkey(fun=snake.up, key='Up')
win.onkey(fun=snake.down, key='Down')
win.onkey(fun=snake.left, key='Left')
win.onkey(fun=snake.right, key='Right')
win.onkey(fun=play_game, key='space')

win.mainloop()
