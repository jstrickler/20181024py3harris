#!/usr/bin/env python

x = 56

if x > 75:
    print("wombat")
    print("wallaby")
elif x > 50:
    print("kangaroo")
    print("koala")
    if x > 50:
        print("blue-footed booby")
else:
    print("kookaburra")


#  FALSE THINGS
#  x == 0     x == 0.0   x == None  X == False
#  len(x) == 0

#    A?B:C

#    B if A else C

entry = 0

limit = entry if entry else 100


# connect(s1 if db == 'sqlite' else s2)

#  == != > < >= <= is

spam = 27

if spam is None:
    print("wahoo")

# if x is False:  # bool(x) is False
#     print("Don't do that!")


x = 5
y = 5

print(x == y)
print(x is y)
print()

name1 = 'Bob'
name2 = 'Bob'
print(name1 is name2)
print(id(name1) == id(name2))

if (name1 == 'Bob') and (y > 0):
    print("wahooooo")

#  and  or  not

print(12 and 5)
print(12 or 5)
print(0 and 5)
print("" and 5)
print(None and 5)

print(not True)
print(not 5)
print(not None)
print(not False, not True, not "False", not "True")




