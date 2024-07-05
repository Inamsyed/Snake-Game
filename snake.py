from turtle import  Turtle
MOVING_DISTANCE = 20
SNAKE_COLOR = "gold"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        tShape = "square"
        tColor = SNAKE_COLOR
        t1 = Turtle(tShape)
        t2 = Turtle(tShape)
        t3 = Turtle(tShape)
        t1.penup()
        t2.penup()
        t3.penup()
        t1.color(tColor)
        t2.color(tColor)
        t3.color(tColor)
        t1.setposition(20, 0)
        t2.setposition(t1.xcor() - 20, t1.ycor())
        t3.setposition(t1.xcor() - 40, t1.ycor())
        self.segments.append(t1)
        self.segments.append(t2)
        self.segments.append(t3)

    def move(self):
        for segNum in range(len(self.segments) - 1, 0, -1):
            newx = self.segments[segNum - 1].xcor()
            newy = self.segments[segNum - 1].ycor()
            self.segments[segNum].goto(newx, newy)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)

    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def collision(self):
        if (self.head.xcor() <= -300 or self.head.xcor() >= 300 or
            self.head.ycor() >= 300 or self.head.ycor() <= -300):
            return True
        for seg in self.segments:
            if(seg != self.head and self.head.distance(seg) < 10):
                return True

    def add_segment(self, position):
        newSegment = Turtle("square")
        newSegment.penup()
        newSegment.color(SNAKE_COLOR)
        newSegment.setposition(position)
        self.segments.append(newSegment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
