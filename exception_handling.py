#!/usr/bin/env python

morph = 22.3

blarks = [5.2, 4.3, 1.1, 0, 8.9, 'abc', 5]

for b in blarks:
    try:
        result = morph / b
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
        break
    except Exception as err:
        print("UNEXPECTED!", err)
    else:
        print(result)
    finally:
        print("*")
