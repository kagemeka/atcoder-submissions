import sys
import numpy as np

n, d, k = map(int, sys.stdin.readline().split())
lr = [(int(l), int(r)) for _ in range(d) for l, r in [sys.stdin.readline().split()]]
s, t = np.array(sys.stdin.read().split(), dtype=np.int32).reshape(k, 2).T

def main():
    res = np.zeros(k, np.int8)
    day = 0
    for l, r in lr:
        day += 1
        movable = (s != t) & (s >= l) & (s <= r)
        arrivable = movable & (t >= l) & (t <= r)
        s[movable & (t < l)] = l
        s[movable & (t > r)] = r
        s[arrivable] = t[arrivable]
        res[arrivable] = day
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
