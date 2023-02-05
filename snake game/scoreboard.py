from turtle import *
from snake import Snake
ALIGMENT = "center"
FONT = ("Courier",21 ,"normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align = ALIGMENT , font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over ", align=ALIGMENT, font=FONT)

    def incrise_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()
