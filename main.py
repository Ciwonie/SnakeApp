"""
Thinking about creating this game:
Start by planning the shape of the snake! Start with 3 squares, approx. 20px.

                        Project Goals:
1. Create a snake body          5. create a scoreboard
2. move the snake               6. detect collision with wall
3. create snake food            7. detect collision with tail
4. Detect collision with food
"""
# GOAL 1 COMPLETE 20 APR 21
# GOAL 2 COMPLETE 20 APR 21
# GOAL 3 COMPLETE 20 APR 21
# GOAL 4 COMPLETE 21 APR 21
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()

        # detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()

    screen.exitonclick()


if __name__ == "__main__":
    main()
