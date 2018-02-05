import re

in_path = "../data/roman_corpus.txt"
out_path = "../res/terminal_freq.csv"

with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()

raw_corpus = raw_corpus.lower()
pattern = "[^a-zA-Z]+"
words = re.split(pattern,raw_corpus)
words = list(filter(None, words))

freq = [0] * 26

for word in words:
    freq[ord(word[-1]) - 97] += 1

with open(out_path, "w") as f:
    f.write(",".join([str(i) for i in freq]))
