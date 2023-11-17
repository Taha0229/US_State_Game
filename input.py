import turtle as t
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data["state"]

states_list = states.to_list()


screen = t.Screen()


class Start_input(t.Turtle):
    def __init__(self):
        super().__init__()
        self.correct_answers = []
        self.remaining_correct_answers = []
        self.hideturtle()
        self.pu()
        self.index_ = 0
        self.score = 0
        screen.title(f"{self.score}/50 States Correct")

    def ask_question(self):
        answer_state = screen.textinput(title="Guess the State", prompt="What's the another states name?").title()
        if answer_state == "Exit":
            for state in states_list:
                if state not in self.correct_answers:
                    self.remaining_correct_answers.append(state)
            exit_message = screen.textinput(title="Exit Message", prompt="Now exiting the game and printing all the "
                                                                         "remaining correct answers").title()
            print(self.remaining_correct_answers)
            return False
        else:
            self.check_answer(answer_state)
            return True

    def check_answer(self, answer_state):
        if answer_state in states_list:
            state_data = data[states == answer_state]
            # print(state_data)
            print("correct")
            self.correct_answers.append(answer_state)
            self.set_score()
            self.index_ = states_list.index(answer_state)
            self.goto(x=int(state_data["x"]), y=int(state_data["y"]))
            self.write(f"{answer_state}", align='center', font=('arial', 8, 'normal'))

        else:
            print("incorrect")

    def set_score(self):
        self.score += 1
        screen.title(f"{self.score}/50 States Correct")

