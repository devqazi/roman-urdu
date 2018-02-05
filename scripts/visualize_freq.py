import matplotlib.pyplot as plt

in_path = "../res/urdu_transitions.csv"


with open(in_path) as f:
    data = f.read()

data = [[int(j) for j in i.split(",")] for i in data.split("\n")]

figure, ax = plt.subplots()
heat_map = ax.pcolor(data)
col_labels = [str(i) for i in range(44)]
row_labels = [str(i) for i in range(44)]
print(col_labels)
ax.set_xticks([i + 0.5 for i in range(44)], minor=False)
ax.set_yticks([i + 0.5 for i in range(44)], minor=False)
ax.set_xticklabels(row_labels)
ax.set_yticklabels(col_labels)
plt.show()
