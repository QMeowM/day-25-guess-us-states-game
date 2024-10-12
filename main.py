import turtle
import pandas
from print_answer import Answer
import time

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"     # GIF is the only image format that works with turtle
screen.addshape(image)
turtle.shape(image)


#
# timer = turtle.Turtle()
# timer.penup()
# timer.hideturtle()
# timer.goto(200, 200)

"""a function that prints out the coordinates where mouse clicks"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()     #or data.state.to_list()
correct_answer = []
score = 0

game_on = True

# start = time.time()
# time_lapse = time.time() - start
# time_left = 300 - time_lapse
# timer.write(arg=f"Time left: {self.time_left} Secs")
while game_on:
    """A prompt to get user's guesses"""
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        edu_list = []
        for state in states:
            if state not in correct_answer:
                edu_list.append(state)
        edu_data = pandas.DataFrame(edu_list)
        edu_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states:

        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data["state"] == answer_state]["y"].item()  # .item() gets the first item in a series
        answer = Answer(x_cor, y_cor, answer_state)
        answer.print_answer()
        correct_answer.append(answer_state)
        score += 1

