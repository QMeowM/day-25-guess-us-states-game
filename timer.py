"""Unfinished currently not used"""

import time
from pyclbr import Class
from turtle import Turtle
from turtledemo.penrose import start

TIME_LIMIT_SECS = 300

class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(200,200)
        self.start = time.time()
        self.time_lapse = time.time() - self.start
        self.time_left = 300 - self.time_lapse
        self.write(arg=f"Time left: {self.time_left} Secs")


