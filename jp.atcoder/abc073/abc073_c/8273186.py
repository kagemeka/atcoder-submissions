from sys import stdin
from collections import Counter

n, *a = (int(x) for x in stdin.read().split())

count = 0
for v in Counter(a).values():
    if v % 2 == 1: count += 1

print(count)
