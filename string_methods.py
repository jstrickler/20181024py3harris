#!/usr/bin/env python

actor = 'Steven Ross Segal'
print(actor)
print(len(actor))

print(actor.upper())
print(actor.count('s'))
print(actor.count('oss'))
print(actor.lower().count('s'))
print(actor.startswith('S'))
print(actor.endswith('z'))

names = actor.split()
print(names)

record = 'up\tup\tand\taway'
words = record.split('\t')
print(words)


print(actor.find('Ross'))
print(actor.index('Ross'))

thing = 'green/blue'

print(thing.partition('/'))


print("/foo/bar/blah".rpartition('/'))


s = "      All my exes live in Texas       "
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print(s.replace(' ', ''))
print(s.replace(' ', '_'))
print()



s = "xyxxyyxxxyyyAll my exes live in Texasxyyyyxxxxxx"
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()
