#!/usr/bin/env python

list1 = list()   #  list list1 = new list()
list2 = ['winkin', 'blinkin', 'nod']
list3 = []
print(id(list1), id(list2), id(list3))
list4 = 'foo:bar:blah'.split(':')
print(list4)

colors = ['red', 'blue', 'green', 'yellow']
print(colors[0], colors[2], colors[3])
# print(colors[99])
print(colors[-1])  # colors[len(colors) - 1]
print(colors[-2])
print(colors[-4])

print(len(colors))

colors.append('purple')
print(colors, '\n')

things = ['Fred', 1, None, True, 5.7]

colors.insert(0, 'ecru')
colors.insert(3, 'chartreuse')
print(colors, '\n')

more_colors = ['navy', 'mauve', 'black']

colors.extend(more_colors)

print(colors, '\n')

del colors[5]

print(colors, '\n')

colors.remove('purple')

print(colors, '\n')

# colors.remove('orange')

c = colors.pop()
print(c)
print(colors, '\n')

c = colors.pop(3)
print(c)
print(colors, '\n')

print(colors.index('blue'))

# print(colors.index('orange'))

print('orange' in colors)  # colors.contains('orange')

# colors.sort()
print(colors)

c = sorted(colors)
print(c)


print("3" > 3)

