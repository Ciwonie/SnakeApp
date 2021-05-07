from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
HEAD = 0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self, fwd_movement=20):

        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(fwd_movement)

    def up(self):
        if self.segments[HEAD].heading() != DOWN:
            self.segments[HEAD].setheading(UP)

    def down(self):
        if self.segments[HEAD].heading() != UP:
            self.segments[HEAD].setheading(DOWN)

    def left(self):
        if self.segments[HEAD].heading() != RIGHT:
            self.segments[HEAD].setheading(LEFT)

    def right(self):
        if self.segments[HEAD].heading() != LEFT:
            self.segments[HEAD].setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]