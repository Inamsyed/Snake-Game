from turtle import  Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("goldenrod1")
        self.speed("fastest")
        self.move()

    def move(self):
        xCor = random.randint(-280, 280)
        yCor = random.randint(-280, 280)
        self.goto(xCor, yCor)