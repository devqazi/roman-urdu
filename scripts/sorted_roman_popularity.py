in_path = "../res/popularity.csv"
out_path = "../res/sorted_roman_pop.csv"

with open(in_path, encoding="utf8") as file:
    raw = file.read()

freqs = [int(i.split(",")[1][1:]) for i in raw.split("\n")[:-1]]
words = [i.split(",")[0] for i in raw.split("\n")[:-1]]

unique_freqs = []

for f in freqs:
    if f not in unique_freqs:
        unique_freqs.append(f)

unique_freqs = sorted(unique_freqs,reverse=True);

map = [[] for i in range(unique_freqs[0] + 1)]

for i,w in enumerate(words):
    map[freqs[i]].append(w)


