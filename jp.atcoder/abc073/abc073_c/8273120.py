from collections import Counter
from sys import stdin

n, *a = (int(x) for x in stdin.read().split())

count = 0
for v in Counter(a).values():
    if v % 2 == 0:
        count += 1

print(count)
