from turtle import Turtle
import random
COLOURS = ["blue", "red", "yellow", "green", "purple", "orange"]


class Cars:

    def __init__(self):
        self.computer_cars = []
        for _ in range(30):
            self.vehicle(random.randint(-400, 400))

    def vehicle(self, x_coord):
        new_vehicle = Turtle("square")
        new_vehicle.penup()
        new_vehicle.goto(x_coord, random.randint(-225, 225))
        new_vehicle.shapesize(1, 2)
        new_vehicle.color(random.choice(COLOURS))
        self.computer_cars.append(new_vehicle)

    def move_cars(self, speed):
        for car in self.computer_cars:
            car.backward(speed)
