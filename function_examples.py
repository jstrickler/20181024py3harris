#!/usr/bin/env python
import typing

# basic function syntax
# return values
# 4 kinds of function parameter definitions
#    default values
# variable scope

def hello_world():
    print("Hello, world")

hello_world()


def hello(whom: str="world") -> None:
    print("Hello,", whom)


hello("world")
hello("Mom")
hello(3.2)
hello(None)
# hello()
# hello('Frank', 'Betty')
hello()

def spam(things: typing.Iterable) -> typing.List[str]:
    pass


#        0  1
def doit(x, y):
    print(f"Doing {x} with {y}")

#    0   1
doit(5, 10)


def greet(greeting, *greetees):
    print("greetees:", greetees)
    for greetee in greetees:
        print(greeting, greetee)


greet("Howdy", "Mom", "Dad", "Sis", "Bro", "Aunt Fanny")


def foo(*, a, b):
    pass

foo(b=10, a="wombat")

def bar(a, b):
    print(a, b)

bar(b="fluffy", a="kittens")
bar("fluffy", "kittens")
print()

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


config(user_name='Aaron', file_name="wombats.txt", surprise="Spanish Inquisition")

def wacky(p1, p2, *p3, p4=5, p5="spam", **p6):
    pass

def thing():
    return 42


x = thing()

print(x)
