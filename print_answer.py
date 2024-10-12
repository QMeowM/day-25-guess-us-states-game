from turtle import Turtle

FONT = ('Arial', 8, 'normal')

class Answer(Turtle):
    def __init__(self,x,y,state):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        self.hideturtle()
        self.penup()

    def print_answer(self):
        self.goto(self.x, self.y)
        self.write(arg=self.state, align="center", font=FONT)