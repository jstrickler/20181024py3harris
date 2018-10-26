#!/usr/bin/env python

john_countries = """Canada
Mexico
Barbados
China
UK
Austria
Spain
Bulgaria
Israel""".split()

clare_countries = """BVI
Denmark
UK
Spain
Kenya
Mexico
Barbados
Norway
Sweden
Canada""".split()

john = set(john_countries)
clare = set(clare_countries)

print('Norway' in john, 'Norway' in clare)
print(len(john), len(clare))

print("both:", clare & john)
print("either:", clare | john)
print("just one:", clare ^ john)
print("Clare only:", clare - john)
print("John only:", john - clare)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = [line.rstrip() for line in breakfast_in]

print(foods)

print(set(foods))


import time

start = time.time()
time.sleep(2.5)
end = time.time()

elapsed = end - start
print("Elapsed:", elapsed)

from timeit import Timer

t = Timer('x = 5', 'import re')

print(t.timeit(100))















