import turtle as t
import input

screen = t.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)
start_input = input.Start_input()
screen.tracer(0)
SCORE = 0

for i in range(50):

    screen.update()
    if start_input.ask_question():
        pass

    else:
        break
