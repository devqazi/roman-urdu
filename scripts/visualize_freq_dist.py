import re
import matplotlib.pyplot as plt

in_path = "../res/freq_map.csv"


with open(in_path) as f:
    data = f.read()

data = [int(j) for j in re.split("[^0-9]+", data)]

# in order of bi_grams
plt.plot(data)
plt.show()

# in order of increasing freq
# plt.show(sorted(data))
# plt.show()
