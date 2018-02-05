import matplotlib.pyplot as plt

in_path = "../res/freq_map.csv"


with open(in_path) as f:
    data = f.read()

data = [[int(j) for j in i.split(",")] for i in data.split("\n")]

for i, row in enumerate(data):
    for j, col in enumerate(data):
        if data[i][j] is not 0:
            data[i][j] = 1

figure, ax = plt.subplots()
heat_map = ax.pcolor(data)
col_labels = [chr(i+65) for i in range(26)]
row_labels = [chr(i+65) for i in range(26)]
print(col_labels)
ax.set_xticks([i+0.5 for i in range(26)], minor=False)
ax.set_yticks([i+0.5 for i in range(26)], minor=False)
ax.set_xticklabels(row_labels)
ax.set_yticklabels(col_labels)
plt.show()
