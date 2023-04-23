from turtle import Turtle
FONT = ("Courier", 18, "normal")
FONT1 = ("Courier", 28, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(-230,270)
        self.hideturtle()
        self.write(f" level : {self.score}", align="center", font=FONT)
    
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f" level : {self.score}", align="center", font=FONT)
    def gameover (self):
        g=Turtle()
        g.penup()
        g.color("black")
        g.goto(0,0)
        g.hideturtle()
        g.write(f"GAME OVER ", align="center", font=FONT1)

        