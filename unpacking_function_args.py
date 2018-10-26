#!/usr/bin/env python

def spam(*things):
    print(things)

spam(1)
spam(1, 2, 3, 4)
spam()
print()
params = [2, 4, 6, 8, 10, 12]

spam(params)
spam(*params[:3])
print()

def config(**kwargs):
    print(kwargs)

config(animal='wombat', music='jazz')

info = {
    "animal": 'gorilla',
    "music": 'ska',
}

config(**info)
