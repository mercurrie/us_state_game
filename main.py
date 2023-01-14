import turtle
import pandas

GAME_TITLE = "US State Game"
IMAGE = "blank_states_img.gif"
PROMPT = "What's another state's name?"
DATA = pandas.read_csv("50_states.csv")
EXIT = "Exit"
STATES_TO_LEARN = "states_to_learn.csv"

screen = turtle.Screen()
screen.title(GAME_TITLE)
screen.addshape(IMAGE)
turtle.shape(IMAGE)
guessed_states = []
all_states = DATA.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", PROMPT).title()

    if answer_state == EXIT:
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(STATES_TO_LEARN)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = DATA[DATA.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)





