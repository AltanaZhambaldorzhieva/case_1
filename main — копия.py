# Case_1
# Zhambaldorzhieva A., Ryaguzova D., Zaytseva D.
#
import turtle
def paral(x,y,a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('purple')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a / 2)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(a / 2)
    turtle.right(135)
    turtle.end_fill()


def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('red', 'red')
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def triangle(x, y, a, linecolor, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color(linecolor, color)
    turtle.begin_fill()
    hyp = a * 2 ** 0.5
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(hyp)
    turtle.left(135)
    turtle.forward(a)
    turtle.end_fill()
    turtle.left(90)

