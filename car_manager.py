
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def move_cars(self):
       for car in self.all_cars:

        car.forward(self.car_speed )
        
    def create_car(self):
        lucky_car = random.randint(1,6)
        if lucky_car == 4: # or lucky_car ==2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.seth(180)
            new_car.penup()
            rand_pos = random.randint(-250, 250)
            new_car.goto(300,rand_pos)
            self.all_cars.append(new_car)

    
    def level_up(self):
        self.car_speed+= MOVE_INCREMENT

    def is_collision(self, player):
        for car in self.all_cars:
            if car.distance(player) < 28:
                return True
        return False
