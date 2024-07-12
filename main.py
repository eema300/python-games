from turtle import Turtle, Screen, reset
from random import randint


# cursor, window objects
win = Screen()
win.setup(width=500, height=400)
win.colormode(255)
win.bgcolor(21, 195, 255)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = [Turtle() for i in range(6)]
for t, c in zip(turtles, colors):
    t.hideturtle()
    t.shape('turtle')
    t.penup()
    t.color(c)

# functions
def race_turtles(turtles, is_race_on, winner):
    # check if reached the finish line
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winner = t.pencolor()
        distance = randint(0, 10)
        t.forward(distance)
    return is_race_on, winner

def reset_race(turtles):
    y = 100
    for t in turtles:
        t.showturtle()
        t.goto(-230, y)
        y -= 40

def check_winner(winner, bet):
    if winner == bet:
        return win.textinput(title='play again?', prompt=f"the winner was {winner}, you won the bet!\n\nwould you like to play again?")
    else:
        return win.textinput(title='play again?', prompt=f"the winner was {winner}, you lost the bet!\n\nwould you like to play again?")

def turtle_race_game(turtles):
    winner = 'none'
    game_on = True
    while(game_on):
        # reset turtle pos
        reset_race(turtles)
        # get user bet
        user_bet = win.textinput(title='make your bet', prompt='which turtle will win the race? enter a color:')
        # set race on/off state
        is_race_on = user_bet is not None
        # RACE
        while(is_race_on):
            is_race_on, winner = race_turtles(turtles, is_race_on, winner)
        # check if bet was right
        play_again = check_winner(winner, user_bet)
        # ask user to start over
        if play_again != 'yes':
            game_on = False

# main logic
win.listen()
turtle_race_game(turtles)
input = win.textinput(title='bye', prompt='shutting down...press enter.')
win.bye()
win.mainloop()