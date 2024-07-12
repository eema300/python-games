import turtle as t
import colorgram as cg
import random as rd

# get colors
colors = cg.extract('d_h_spot.jpeg', 32)
rgb_vals = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# create turtle and canvas
tr = t.Turtle()
win = t.Screen()
win.bgcolor("white")
win.setup(500, 500)

# set starting characteristics
tr.hideturtle()
tr.penup()
tr.goto(-225, -225)
t.colormode(255)
rd.seed(a=25)

# draw dots
count = 1
for _ in range(100):
  tr.dot(20, rd.choice(rgb_vals))
  if count % 10 == 0:
    tr.goto(tr.pos()[0] - 450, tr.pos()[1] + 50)
    count += 1
    continue
  tr.forward(50)
  count += 1    

t.mainloop()
win.exitonclick()
