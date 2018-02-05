import re

in_file = "../data/wordlist.txt";

with open(in_file, encoding="utf8") as f:
    raw = f.read().split("\n");

print(len(raw))
