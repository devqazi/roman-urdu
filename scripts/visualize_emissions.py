import matplotlib.pyplot as plt
import re

in_path = "../res/urdu_terminals.json"

with open(in_path) as f:
    raw = f.read()

data = re.finditer(": (\d+)",raw);
data = [int(i.group(1)) for i in data]

labels = re.findall('u.{4}',raw)
ticks = range(41)

plt.bar(ticks, data, align="center")
plt.xticks(ticks, labels)
plt.title("Emission frequencies")
plt.show()
