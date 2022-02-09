import sys
n, m, *ab = (int(x) for x in sys.stdin.read().split())
from_1, to_n = set(), set()
for a, b in zip(*[iter(ab)] * 2):
    if a == 1: from_1.add(b)
    elif b == n: to_n.add(a)
print('POSSIBLE' if from_1 & to_n else "IMPOSSIBLE")
# & は bloolean operator and ではなく set間で使われるoperator、
# intersections が存在すればそれらのsetを返す。
