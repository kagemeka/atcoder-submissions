import sys
n, m, *ab = map(int, sys.stdin.read().split())
from_1, to_n = set(), set()
for a, b in zip(*[iter(ab)] * 2):
    if a == 1: from_1.add(b)
    if b == n: to_n.add(a)
print('POSSIBLE' if from_1 & to_n else "IMPOSSIBLE")
