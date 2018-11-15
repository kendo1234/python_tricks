#!/user/bin/env python

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print("passed")

if 1 in (x, y, z):
    print("passed")

# This only tests for truthiness
if any((x, y, z)):
    print("passed")