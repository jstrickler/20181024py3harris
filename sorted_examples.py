#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f0 = sorted(fruits)
print("f0:", f0, '\n')

f1 = sorted(fruits, key=str.lower)
print("f1:", f1, '\n')

def ignore_case(one_element):
    return len(one_element)

f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def length_and_name(e):
    return len(e), e.lower()

f4 = sorted(fruits, key=length_and_name)
print("f4:", f4, '\n')


values = [1, 'fish', 200, 'blue', None, 5.6]

def mixed(e):
    return str(e).lower()

v1 = sorted(values, key=mixed)
print("v1:", v1, '\n')

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
print()
for first_name, last_name, _ in sorted(people):
    print(first_name, last_name)
print()

def by_last_name(person):
    return person[1], person[0]

for first_name, last_name, _ in sorted(people, key=by_last_name):
    print(first_name, last_name)
print()

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'MCO': 'Orlando',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

for abbr, airport in sorted(airports.items()):
    print(abbr, airport)
print()


for abbr, airport in sorted(airports.items(), key=lambda e: (e[1], e[0]), reverse=True):
    print(abbr, airport)
print()
