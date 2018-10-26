#!/usr/bin/env python

from collections import Counter


with open('DATA/words.txt') as words_in:
    word_list = (line[0] for line in words_in)
    letter_counts = Counter(word_list)

print(letter_counts)

