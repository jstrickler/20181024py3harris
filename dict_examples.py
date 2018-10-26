#!/usr/bin/env python
from pprint import pprint

d1 = dict()
d2 = {'red': 5, 'purple': 6, 'pink': 8, 'orange': 2}
d3 = {}
d4 = dict(red=5, purple=6, pink=8, orange=2)

pairs = [('red', 5), ('purple', 6), ('pink', 8), ('orange', 2)]
d5 = dict(pairs)

print(d2)
print(d4)
print(d5)

colors = 'red purple pink orange'.split()
values = 5, 6, 8, 2

d6 = dict(zip(colors, values))
print(d6)

print(list(zip(colors, values)))

airports = {
    'EWR': 'Newark',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}
print(airports)
print(airports['RDU'])
print(airports['EWR'])
#print(airports['MLB'])
print(airports.get('MLB', 'Melbourne'))
print(airports.get('MLB'))
print(airports.setdefault('MLB', 'Melbourne'))
airports['MCO'] = 'Orlando'
print(airports)
# airports['MCO'] = 'Mouseville'

pprint(airports)

print('MCO' in airports)
print(airports.keys())
print(airports.values())

print(airports.items())

# for k, v in DICT.items()
for wombat, geoduck in sorted(airports.items()):
    print(wombat, geoduck)

del airports['MCO']
pprint(airports)

more_airports = {'HLN': 'Helena', 'ELM': 'Elmyra/Corning',
                 'ALB': 'Albany', 'MLB': 'Space Coast'}

airports.update(more_airports)

pprint(airports)
