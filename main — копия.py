# Case_1
# Zhambaldorzhieva A., Ryaguzova D., Zaytseva D.
#
import turtle

turtle.speed(1000)


def paral(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('dark blue')
    turtle.begin_fill()
    turtle.forward(a / 2)
    turtle.left(135)
    turtle.forward((a / 2) * 2 ** 0.5)
    turtle.left(45)
    turtle.forward(a / 2)
    turtle.left(135)
    turtle.forward((a / 2) * 2 ** 0.55)
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


main()

# one

turtle.left(90)
triangle(150, -150, 50, 'blue', 'blue')
turtle.left(90)
triangle(150, -150, 25, 'orange', 'orange')
turtle.right(45)
triangle(150, -175, 35.35, 'red', 'red')
turtle.left(135)
paral(125, -200, 50)
turtle.left(180)
triangle(150, -250, 50, 'green', 'green')
square(152, -250, 25)
turtle.left(180)
triangle(100, -225, 25, 'purple', 'purple')

# zero

square(20, 250, 40)
turtle.right(135)
triangle(78, 267, 80, 'orange', 'orange')
turtle.left(45)
triangle(57, 323, 35, 'purple', 'purple')
turtle.left(45)
triangle(22, 358, 50, 'red', 'red')
turtle.left(45)
triangle(-19, 358, 38, 'blue', 'blue')
turtle.left(45)
triangle(-90, 285, 100, 'green', 'green')


