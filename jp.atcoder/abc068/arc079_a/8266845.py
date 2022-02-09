import sys
l = sys.stdin.readlines()
n, m = l[0].split()

from_1, to_n = set(), set()
for a, b in (l[i].split() for i in range(1, int(m)+1)):
    if a == '1': from_1.add(b)
    elif b == n: to_n.add(a)

print("POSSIBLE" if from_1 & to_n else "IMPOSSIBLE")
