#!/usr/bin/env python

actor = 'Steven Segal'
a = 5
b = 234.595

print(actor, a, b)

print(actor, a, b, sep=":")

print(actor, a, b, sep=" wombat nuggets ")

print(actor, end="=>")
print(a, end="<=")
print(b)

x = "foo\n"
y = "bar\n"

print(x, end='')
print(y, end='')

# print(..., end='\n', sep=' ', flush=False,
#     file=sys.stdout)

print(a, b)
#         0      1           0  1
print('{:03d} {:.1f}'.format(a, b))
print('%03d %.1f' % (a, b))
print(f'{a:03d} {b:.1f}')

print("From the {0} of {1} {0}".format('department',
                                       'redundancy'))

