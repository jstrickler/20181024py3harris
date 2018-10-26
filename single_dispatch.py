#!/usr/bin/env python
#
from singledispatch import singledispatch
from io import TextIOWrapper


@singledispatch
def xopen(source, mode="r"):  # <1>
    source_type = type(source).__name__
    raise TypeError("Invalid arg: must be file, str, or bytes, not", source_type)


@xopen.register(TextIOWrapper)  # <2>
def xopen_file(fileobj):
    return fileobj


@xopen.register(str)  # <3>
def xopen_str(str, mode="r"):
    return open(str, mode)


@xopen.register(bytes)  # <4>
def xopen_bytes(bytes, mode="r"):
    return open(bytes.decode(), mode)


mary_in = open('DATA/mary.txt')  # <5>

for x in mary_in, 'DATA/mary.txt', b'DATA/mary.txt', 52:
    try:
        file_in = xopen(x)  # <6>
        result = file_in.read()
        print("Length: {}".format(len(result)))
    except TypeError as err:
        print('ERROR:', err)

print('-' * 60)
print(xopen.dispatch(str), "\n")  # <7>
for arg_type, func in xopen.registry.items():
    print(arg_type, func)  # <8>

with xopen('DATA/mary.txt') as mary_in:
    pass
