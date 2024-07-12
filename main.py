from turtle import Turtle, Screen


# cursor, window objects
t = Turtle()
win = Screen()
t.speed(0)
win.setup(500, 500)


# functions
def move_forwards():
    t.forward(1)

def move_backwards():
    t.backward(1)

def counter_clockwise():
    t.left(10)

def clockwise():
    t.right(10)

def exit_program():
    win.bye()


# main logic
win.listen()
win.onkey(key="w", fun=move_forwards)
win.onkey(key="s", fun=move_backwards)
win.onkey(key="a", fun=counter_clockwise)
win.onkey(key="d", fun=clockwise)
win.onkey(key="c", fun=t.reset)
win.onkey(key="q", fun=exit_program)
win.mainloop()