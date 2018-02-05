import re

in_path = "../data/roman_corpus.txt"
out_path = "../data/unique_words.csv"
with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()


raw_corpus = raw_corpus.lower()
pattern = "[^a-zA-Z]+"
words = re.split(pattern,raw_corpus)

unique_words = []

for word in words:
    if word not in unique_words:
        unique_words.append(word)

with open(out_path , "w") as f:
    f.write("\n".join(unique_words))

