#!/usr/bin/env python

def opentrim(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip()


mary_in = opentrim('DATA/mary.txt')
for line in mary_in:
    print(line)


def conan():
    words = 'what is best in life'.split()
    for word in words:
        yield word

for w in conan():
    print(w)

def simple():
    yield 'one'
    yield 'two'
    raise StopIteration()
    yield 'three'

for x in simple():
    print(x)
print()

s = simple()
print(next(s))
print(next(s))
try:
    print(next(s))
except StopIteration:
    print("ALL DONE")


foo = ['a', 'b', 'c']
foo_iter = iter(foo)
print(next(foo_iter))
print(next(foo_iter))


