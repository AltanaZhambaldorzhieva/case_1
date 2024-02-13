# Case_1
# Zhambaldorzhieva A., Ryaguzova D., Zaytseva D.
#
import turtle
def paral(x,y,a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('dark blue')
    turtle.begin_fill()
    turtle.forward(a / 2)
    turtle.left(135)
    turtle.forward((a/2)*2**0.5)
    turtle.left(45)
    turtle.forward(a / 2)
    turtle.left(135)
    turtle.forward((a/2)*2**0.55)
    turtle.left(45)
    turtle.end_fill()
    turtle.up()


def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('yellow', 'yellow')
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
    turtle.up()

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
    turtle.up()


def main():
    '''
    Main function.
    :return: None
    '''
    triangle(0, 0, 150, 'pink', 'pink')
    turtle.left(90)
    triangle(0, 0, 150, 'blue', 'blue')
    turtle.right(90)
    square(0, 0, 150 // 2)
    turtle.forward(150 // 2)
    turtle.right(90)
    triangle(150 // 2, 0, 150 // 2, 'orange', 'orange')
    turtle.right(90)
    turtle.forward(150 // 2)
    triangle(0, 0, 150 // 2, 'green', 'green')
    turtle.forward(150 // 2)
    paral(-150 // 2, 0, 150)
    turtle.forward(150 // 2)
    turtle.left(135)
    turtle.forward(2 * (150 / 2) * 2 ** 0.5)
    turtle.left(90)
    triangle(0, -150, (150 / 2) * 2 ** 0.5, 'red', 'red')
    turtle.right(45)
    turtle.forward(150)
    turtle.done()

main()




