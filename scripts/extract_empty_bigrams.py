import re

in_path = "../res/freq_map.csv"
out_path = "../res/empty_bigrams.csv"

with open(in_path) as f:
    data = f.read()

data = [[int(j) for j in i.split(",")] for i in data.split("\n")]

empty_bigrams = []

for i,row in enumerate(data):
    for j,col in enumerate(row):
        if data[i][j] is 0:
            empty_bigrams.append(chr(i + 97) + chr(j + 97))

with open(out_path, "w") as f:
    f.write(",".join(empty_bigrams))
