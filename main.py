import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].tolist()
score = 0
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{score}/50 States Correct", "Name another state?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        state_chosen = data[data.state == answer_state]
        answer_text = turtle.Turtle()
        answer_text.penup()
        answer_text.hideturtle()
        x_coordinate = int(state_chosen.x.iloc[0])
        y_coordinate = int(state_chosen.y.iloc[0])
        answer_text.goto(x_coordinate, y_coordinate)
        answer_text.write(answer_state)
        score += 1
        guessed_states.append(answer_state)
        state_list.remove(answer_state)

screen.bye()

with open("states_to_learn.csv", "w") as file:
    for each_state in state_list:
        if each_state not in guessed_states:
            file.write(each_state + "\n")

