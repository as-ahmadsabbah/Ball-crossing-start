from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.goto(STARTING_POSITION)
        self.color("red")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
    
    def move(self):
        x=self.xcor()
        y=self.ycor()+MOVE_DISTANCE
        self.goto(x,y)


