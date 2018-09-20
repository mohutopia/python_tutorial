import turtle
t = turtle.Pen()

def square(side):
 for i in range(0,4):
  t.forward(side)
  t.left(90)

square(10)
square(50)
square(100)
square(150)
square(250)

def circle(radius):
 t.circle(radius)