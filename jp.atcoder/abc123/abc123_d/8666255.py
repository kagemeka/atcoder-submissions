import sys
import numpy as np
from heapq import heappush, heappop


def main():
    x, y, z, K = map(int, sys.stdin.readline().split())
    abc = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = abc[:x]
    b = abc[x:x + y]
    c = abc[x + y:x + y+ z]
    a = np.sort(a)[::-1]
    b = np.sort(b)[::-1]
    c = np.sort(c)[::-1]

    hq = []
    heappush(hq, (-(a[0]+b[0]+c[0]), 0, 0, 0))
    res = []
    added_before = set()
    # setで確認をO(1)でする
    added_before.add((0, 0, 0))

    for _ in range(K):
        sum_deli, i, j, k = heappop(hq)
        res.append(-sum_deli)
        if i < x - 1 and not (i+1, j, k) in added_before:
            heappush(hq, (-(a[i+1]+b[j]+c[k]), i+1, j, k))
            added_before.add((i+1, j, k))
        if j < y - 1 and not (i, j+1, k) in added_before:
            heappush(hq, (-(a[i]+b[j+1]+c[k]), i, j+1, k))
            added_before.add((i, j+1, k))
        if k < z - 1 and not (i, j, k+1) in added_before:
            heappush(hq, (-(a[i]+b[j]+c[k+1]), i, j, k+1))
            added_before.add((i, j, k+1))

    for s_deli in res:
        print(s_deli)

if __name__ == "__main__":
    main()
