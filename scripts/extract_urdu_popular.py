import re

in_path = "../data/poplist.txt"
out_path = "../res/urdu_popular.tsv"
with open(in_path, encoding="utf8") as file:
    raw_corpus = file.read()

raw_corpus = raw_corpus.lower()
num_pattern = "[0-9]+"
non_num_pattern = "[^0-9]+";
words = re.split(num_pattern,raw_corpus)
words = words[1:]
numbers = re.split(non_num_pattern,raw_corpus)
numbers = numbers[1:-1]

for i,w in enumerate(words):
    words[i] = w.strip()

for i,n in enumerate(numbers):
    numbers[i] = n.strip()

writable = ""

for i,w in enumerate(words):
    writable += w + "\t" + numbers[i] + "\n";

with open(out_path,"w",encoding="utf8") as f:
    f.write(writable)
