from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.player_level()

    def player_level(self):
        self.clear()
        self.goto(-225, 250)
        self.write(f"Level : {self.level}", align="center", font=("Courier", 20, "normal"))

    def add_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
