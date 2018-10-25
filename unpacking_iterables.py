#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

print(person[0], '\n')
# person[0] = 'Melinda'

first_name, last_name, product = person   # iterable unpacking


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
    ('Linus', 'Torvalds', 'Linux', 'Git'),
    ('John', 'Doe'),
]

for first_name, last_name, *_ in people:
    print(first_name, last_name) # , product)



values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)
print()

things = [(0, 'red'), (1, 'blue'), (2, 'purple'), (3, 'orange') ]

for x, y in things:
    print(x, y)
print()

colors = ['red', 'blue', 'purple', 'orange']
for i, color in enumerate(colors):
    print(i, color)

print(list(enumerate(colors)))

print(len(colors), min(colors), max(colors))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(nums), min(nums), max(nums), sum(nums))
print(sum(nums) / len(nums))

print(sorted(colors))
print(sorted(nums), '\n')

print("abc" + "def")
print([0, 1, 2] + ['a', 'b', 'c'])

flags = [True] * 10
print(flags)

print(['a', 'b', 'c'] * 3)

print('-' * 60)

print('PYTHON! ' * 100)

#  range(STOP)   range(START, STOP)  range(START, STOP, STEP)

r = range(1000000)
print(r)

e = enumerate(colors)
print(e)


print(next(e))
print(next(e))

# for foo in bar:
#     print(foo)

# while True
#     try:
#         foo = next(bar)
#     except StopIteration:
#         break


e = enumerate(colors)
ee = e

