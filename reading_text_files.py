#!/usr/bin/env python
# from some_module import (
#     a,
#     b,
#     c,
#     c
# )


with open('DATA/mary.txt', "r") as mary_in:
    for raw_line in mary_in:
        print(raw_line, end='')
print('-' * 60)

#  with EXPR: pass
#  with EXPR as VAR: pass


#    print(hasattr(mary_in, '__exit__'))  # "implements the context interface"

with open('DATA/mary.txt', "r") as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt', "r") as mary_in:
    all_contents = mary_in.read()
    print(repr(all_contents))
    print()
    print(all_contents)
print('-' * 60)


# with open....
#     with open ....
#         with open ....
#
# with (open x as y,
#       open a as b,
#       open r as s):

#  (expr for VAR in ITERABLE)

#   str(x)   repr(x)

x = "spam"

print(x)
print(str(x))
print(repr(x))


with open('DATA/mary.txt', "r") as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)

print('-' * 60)


with open('DATA/mary.txt', "r") as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)

print('-' * 60)

with open('DATA/mary.txt', "r") as mary_in:
    all_lines_without_nl = (line.rstrip() for line in mary_in)
    print(all_lines_without_nl)

print('-' * 60)

with open('DATA/mary.txt', "r") as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)

print('-' * 60)

with open('DATA/words.txt') as words_in:
    for line in words_in:
        if "dog" in line:
            print(line.rstrip())

