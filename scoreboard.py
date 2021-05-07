from turtle import Turtle
import pickle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
X_SCOREBOARD = 0
Y_SCOREBOARD = 260
SCOREBOARD_COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file="data.txt", mode="rb") as HIGHEST:
            try:
                msg = pickle.load(HIGHEST)
                self.high_score = int(msg)
            except Exception as e:
                self.high_score = 0

        self.color(SCOREBOARD_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(X_SCOREBOARD, Y_SCOREBOARD)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_high_score(self):
        try:
            with open(file="data.txt", mode="wb") as HIGHEST:
                msg = pickle.dumps(str(self.high_score))
                HIGHEST.write(msg)
        except Exception as e:
            print(e)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
