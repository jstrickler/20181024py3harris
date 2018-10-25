#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[0], fruits[5], fruits[-1])

#  SEQUENCE[START:STOP]
#  S[:STOP] S[START:]
#  S[START:STOP:STEP]

print(fruits[0:5])
print(fruits[:5])
print(fruits[7:11])

actor = 'Steven Segal'

print(actor[:5])
print(actor[-5:])
print(actor[7:10])

print(actor[10:7:-1])

print(actor[::2])
print()

for fruit in fruits:
    print(fruit)

# for VAR in ITERABLE:
#     ...

for fruit in fruits[:10]:
    print(fruit, end=' ')
print('\n\n')

for i in range(10):
    print("Python is cool")

for i in range(5, 101, 5):
    print(i, end=',')
print('\n\n')

for i, fruit in enumerate(fruits):
    print(i, fruit)
