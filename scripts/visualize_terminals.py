import matplotlib.pyplot as plt

in_path = "../res/terminal_freq.csv"

with open(in_path) as f:
    data = f.read()

data = [int(i) for i in data.split(",")]

labels = [chr(i+97) for i in range(26)]
ticks = range(26)

plt.bar(ticks, data, align="center")
plt.xticks(ticks, labels)
plt.title("Terminal frequencies")
plt.show()