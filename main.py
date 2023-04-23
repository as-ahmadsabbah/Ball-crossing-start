import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car=CarManager()
player=Player()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True
speed=0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.cr()
    car.move(speed)
    for crs in car.CAR_ARRAY:
        if player.distance(crs)<20:
            scoreboard.gameover()
            game_is_on=False
    if player.ycor()>290:
        player.goto(0,-280)
        scoreboard.increase_score()
        speed+=5






screen.exitonclick()