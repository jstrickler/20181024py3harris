#!/usr/bin/env python


def get_long_words():
    with open('DATA/words.txt') as words_in:
        my_generator = (line.rstrip() for line in words_in if len(line) > 15)
        return my_generator
