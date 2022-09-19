from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def mover_adelante():
    tim.forward(10)

def mover_abajo():
    tim.backward(10)

def mover_izquierda():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def mover_derecha():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(mover_adelante, "Up")
screen.onkey(mover_abajo, "Down")
screen.onkey(mover_izquierda, "Left")
screen.onkey(mover_derecha, "Right")
screen.onkey(clear, "c")

screen.exitonclick()