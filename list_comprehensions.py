#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

#  [EXPR for VAR ... in ITERABLE if ... if ... ]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print('f2:', f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]

print('f3:', f3, '\n')

food = ['burger', 'spam', 'spam', 'pizza', 'spam', 'sushi', 'chicken', 'spam', 'spam']

food = [f for f in food if f != 'spam']
print(food)


food_gen = (f for f in food if f != 'spam')
print(food_gen)
for f in food_gen:
    print(f)


people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names_gen = (p[1] for p in people)

colors = ['red', 'blue', 'green']

color_gen = (c.upper() for c in colors)

del colors


print(list(color_gen))





