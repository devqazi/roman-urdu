import re

in_path = "../data/roman_corpus.txt"
out_path = "../res/word_len_dist.csv"
with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()


raw_corpus = raw_corpus.lower()
pattern = "[^a-zA-Z]+"
words = re.split(pattern,raw_corpus)

word_sizes = [0] * 16

for word in words:
    word_sizes[len(word)] += 1

with open(out_path, "w") as f:
    f.write(",".join([str(i) for i in word_sizes]))
