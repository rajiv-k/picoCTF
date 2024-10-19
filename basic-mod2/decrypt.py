#!/usr/bin/env python3

with open("message.txt", 'r') as f:
    line = f.read()
    numbers = map(int, line.split())
    for n in numbers:
        remainder= n%41
        # compute modulo-inverse of the remainder
        remi= pow(remainder, -1, 41)
        if remi >= 1 and remi <= 26:
            print(chr(ord('a') + remi- 1), end="")
        elif remi>= 27 and remi <= 36:
            print(remi-27, end="")
        elif remi== 37:
            print("_", end="")
