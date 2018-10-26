#!/usr/bin/env python


with open('../DATA/fruit.txt') as fruit_in:

    ufruits = (fruit.rstrip().upper() for fruit in fruit_in)

    print(ufruits)

    for f in ufruits:
        print(f)
