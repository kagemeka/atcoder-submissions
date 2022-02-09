import sys
import math

x, y = [int(x) for x in sys.stdin.readline().split()]

count = 0
while x <= y:
    count += 1
    x *= 2

print(count)
