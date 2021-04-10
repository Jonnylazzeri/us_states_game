import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

score = 0
answered_states = []
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data.state.to_list()

while score < 50:
    answer_state = screen.textinput(title=f"Guess the State {score}/{len(states)}", prompt="What's another state's name?")
    if answer_state == 'exit':
        break
    if answer_state.title() in states and answer_state.title() not in answered_states:
        answered_states.append(answer_state.title())
        x = int(data[data.state == answer_state.title()].x)
        y = int(data[data.state == answer_state.title()].y)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(answer_state.title(), align="center")
        score += 1


for state in answered_states:
    if state in states:
        states.remove(state)

data_dict = {
    'States to Learn': states
}
data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")
print(data)