from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center")
        self.hideturtle()

    def increase_score(self):
        self.score += 1
