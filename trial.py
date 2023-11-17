import pandas as pd

data = pd.read_csv("50_states.csv")

states = data["state"]
x_cor = data["x"]
y_cor = data["y"]
data_list = states.to_list()
x_cor_list = x_cor.to_list()
y_cor_list = y_cor.to_list()

print(data_list)
ask = input("enter state ")
if ask in data_list:
    print("yes")
    # print(data_list.index("Alaska"))
    index_state = data_list.index(ask)
    print(x_cor_list[index_state])
    print(y_cor_list[index_state])

