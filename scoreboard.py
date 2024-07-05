from turtle import Turtle
ALIGNMNET = "center"
COLOR = "white"
FONT = ("Courier", 20, "normal")
class Score:

    def __init__(self):
        self.score = Turtle()
        self.endScore = Turtle()
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 260)
        self.scoreNum = 0
        self.score.color(COLOR)
        self.display_score()

    def display_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.scoreNum}", align=ALIGNMNET, font=FONT)

    def update_score(self):
        self.scoreNum += 1
        self.display_score()

    def game_over(self):
        self.score.goto(0,0)
        self.score.write(f"GAME OVER", align=ALIGNMNET, font=FONT)