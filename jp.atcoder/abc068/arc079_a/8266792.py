import sys
from collections import deque
l = deque(sys.stdin.readlines())
n, m = (int(x) for x in l[0].split())
l.popleft()

from_1, to_n = set(), set()
for a, b in deque((int(x) for x in l[i].split()) for i in range(m)):
    if a == 1: from_1.add(b)
    elif b == n: to_n.add(a)

print("POSSIBLE" if from_1 & to_n else "IMPOSSIBLE")
