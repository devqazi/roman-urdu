import re

in_path = "../data/roman_corpus.txt"
out_path = "../res/freq_map.csv"
with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()

raw_corpus = raw_corpus.lower()
pattern = "[^a-zA-Z]+"
words = re.split(pattern, raw_corpus)

for word in words:
    i = 0
    while i < len(word) - 1:
        r = ord(word[i]) - 97
        c = ord(word[i+1]) - 97
        freq[r][c] += 1
        i += 1

writable = ""

for row in freq:
    writable += ",".join([str(i) for i in row])
    writable += "\n"

with open(out_path, "w") as f:
    f.write(writable)
