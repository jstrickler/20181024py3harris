#!/usr/bin/env python
from pprint import pprint

def main():
    data = read_data()

    pretty_print(data)
    print_titles(data)
    print()
    print(get_field(data, 'Lancelot', 2))


def read_data():
    info = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')

            info[name] = title, color, quest, comment

    return info

def pretty_print(knight_info):
    pprint(knight_info)
    print('\n')

def print_titles(knight_info):
    for knight_name, info in knight_info.items():
        print(info[0], knight_name)

def get_field(knight_info, knight_name, field_number):
    return knight_info[knight_name][field_number]

if __name__ == '__main__':
    main()

