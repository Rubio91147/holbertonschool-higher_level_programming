#!/usr/bin/python3
for item in range(100):
    print("{:02d}".format(item), end=", " if item < 99 else "\n")
