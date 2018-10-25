#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in sorted(fruits):
        record =  fruit.upper() + '\n'
        fruitlist_out.write(record)

