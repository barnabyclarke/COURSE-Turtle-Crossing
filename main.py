from turtle import Screen
from cars import Cars
from scoreboard import Scoreboard
from player import Player
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Turtle Crossing")

scoreboard = Scoreboard()
cars = Cars()
player = Player()

screen.listen()
screen.onkey(player.move, "Up")

spawn_rate = 15
speed = 5

alive = True
while alive:
    screen.update()
    time.sleep(0.1)
    scoreboard.player_level()
    cars.move_cars(speed)

    if random.randint(0, 100) <= spawn_rate:
        cars.vehicle(400)

    for x in cars.computer_cars:
        if 25 >= x.xcor() >= -25 and 15 >= (player.ycor() - x.ycor()) >= -15:
            player.color("red")
            scoreboard.game_over()
            screen.update()
            alive = False

    if player.ycor() >= 275:
        scoreboard.add_level()
        player.goto(0, -275)
        time.sleep(0.5)
        speed += 4
        spawn_rate += 5

screen.exitonclick()
