from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

gameIsOn = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while(gameIsOn):
    screen.update()
    time.sleep(0.1)
    snake.move()

    if(snake.head.distance(food) < 15):
        food.move()
        snake.extend()
        score.update_score()

    if(snake.collision() == True):
        score.game_over()
        gameIsOn = False









screen.exitonclick()
