#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

target = 'a'

for fruit in fruits:
    if fruit.startswith(target):
        try:
            print(fruit)
            break
        except Exception as err:
            print(err)
            break
else:
    print("not found")
