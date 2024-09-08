from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def reset_game():
    snake.reset()
    food.refresh()
    scoreboard.reset()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    if 10<=len(snake.segments)<=20:
        time.sleep(.1)
    elif 20<=len(snake.segments)<=30:
        time.sleep(.099999)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        reset_game()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            reset_game()

screen.exitonclick()