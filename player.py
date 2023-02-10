from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.penup()
        self.goto(0, -275)

    def move(self):
        self.forward(20)
