#!/bin/python3

import sys


n = int(input().strip())
binary = []
while n > 0:
    remainder = n % 2
    n = n / 2
    binary.append(remainder)

for numbers in binary:
    print(numbers, sep='')