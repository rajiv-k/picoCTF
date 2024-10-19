#!/usr/bin/env python3

with open("message.txt", 'r') as f:
    line = f.read()
    numbers = map(int, line.split())
    for n in numbers:
        remainder = n%37
        if remainder >= 0 and remainder <= 25:
            print(chr(ord('A') + remainder), end="")
        elif remainder >= 26 and remainder <= 35:
            print(remainder-26, end="")
        elif remainder == 36:
            print("_", end="")
