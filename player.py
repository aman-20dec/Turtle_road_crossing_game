from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
    
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.start_pos()
        

    def move(self):
        self.forward(MOVE_DISTANCE)
        

    def start_pos(self):

        self.goto(STARTING_POSITION)
    
    def is_finish(self):
        return self.ycor() >= FINISH_LINE_Y