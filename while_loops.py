#!/usr/bin/env python


while True: # {
    file_name = input("Enter file to process (or q to quit): ")
    if file_name == 'q':
        break
    if file_name == '':
        continue
    print("processing", file_name)
# }
