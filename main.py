import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, key="Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move_cars()

    if player.is_finish():
            player.start_pos()
            cars.level_up()
            scoreboard.level_up()

    if cars.is_collision(player):
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()