import matplotlib.pyplot as plt

in_path = "../res/word_len_dist.csv"

with open(in_path) as f:
    data = f.read()

data = [int(i) for i in data.split(",")]

# by increasing length
plt.plot(data)
plt.show()

# by increasing sizes
plt.plot(sorted(data))
plt.show()