import re

in_path = "../data/roman_corpus.txt"
out_path = "../res/popularity.csv"
with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()

raw_corpus = raw_corpus.lower()
pattern = "[^a-zA-Z]+"
words = re.split(pattern, raw_corpus)

map = {}

for w in words:
    if w not in map:
        map[w] = 1;
    else:
        map[w] += 1;



writable = ""
for item in map.items():
    writable += item[0] + ", " + str(item[1]) + "\n"

with open(out_path , "w") as f:
    f.write(writable)

