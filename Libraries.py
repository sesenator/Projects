import turtle

turtle.shape("turtle")

turtle.penup()
turtle.forward(-150)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.pendown()

for i in range(4):
    turtle.forward(300)
    turtle.right(90)

turtle.right(-45)
turtle.forward(212.13)
turtle.right(90)
turtle.forward(212.13)

turtle.penup()
turtle.right(45)
turtle.forward(300)
turtle.left(90)
turtle.forward(-125)
turtle.pendown()

turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)


turtle.penup()
turtle.forward(-200)
turtle.pendown()

def main():
    window()
def window():
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    for i in range(4):
        turtle.forward(50)
        turtle.right(90)
    lines()

def lines():
    turtle.penup()
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.pendown()
    for i in range(4):
        turtle.forward(25)
        turtle.right(90)
        turtle.forward(25)



if __name__ == "__main__":
    main()
    lines()

turtle.done()
