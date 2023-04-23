from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.CAR_ARRAY=[]
    def cr (self):
        if random.randint(1,5)==1:
            car=Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300, random.randint(-250, 250)) 
            self.CAR_ARRAY.append(car) 
    def move (self,speed) :
        for car1 in self.CAR_ARRAY :
            car1.backward(STARTING_MOVE_DISTANCE+speed)



