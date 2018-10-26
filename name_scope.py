#!/usr/bin/env python
"""
Exciting examples for Harris Python class
"""
import sys

x = 100  # GLOBAL variable

# def print(*args):
#     sys.stdout.write("HA HA HA!\n")

stuff = []

def spam():
#    global x  # DON'T!!! REALLY, DON'T!!!!!
#    x = -3
    y = 42  # LOCAL variable
    stuff.append("wow!")
    print("in spam(): x is", x)


spam()
# print("in main: y is", y)

print("in main: x is", x)
print(stuff)

#  local, nonlocal, global, builtin

def outer():
    """
    Example for nested function calls.

    To use, call outer() and use the return value.

    :return: function object that has name embedded within.
    """
    name = 'Bob'  # nonlocal scope

    def inner():
        print("My name is", name)

    # inner()

    return inner  # return function *object*, don't *call* function


i = outer()
i()



def ham(file_name):
    """
    Process blarch files

    :param file_name: File to open -- must be in blarch format
    :return:
    """
    pass



