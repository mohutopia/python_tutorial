import turtle
t = turtle.Pen()

for i in range(0,38):
 t.forward(100)
 t.left(175)
# draws a sort of star on: Python Turtle Graphics

# to lift the pen up and change its location if we want
t.up()
t.forward(140)
# to put the pen back down and start drawing
t.down()
for i in range(0,38):
 t.forward(100)
 t.left(175)

t.reset() # to reset everything

# start new drawing of a boxy car
t.color(0,0,1) # RGB based, so the color is blue
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(30)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(70)
t.left(90)
t.forward(40)
t.right(90)
t.forward(40)
t.left(90)
t.forward(30)
t.end_fill() # the object created from the .begin_fill() will be colored

# draw the two wheels
t.up()
t.left(90)
t.forward(40)
t.right(90)
t.forward(15)
t.color(0,0,0) # color: black
t.down()
t.begin_fill()
t.circle(15) # to draw a circle with a radius of 15px
t.end_fill()

t.up()
t.left(90)
t.forward(70)
t.begin_fill()
t.down()
t.right(90)
t.circle(15)
t.end_fill()