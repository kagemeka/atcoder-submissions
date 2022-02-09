# 2019-11-24 13:14:50(JST)
import sys
import numpy as np

def main():
    s, t, u, v, T, V = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().rstrip())

    x, y = [], []
    for i in range(n):
        xy = sys.stdin.readline().split()
        x.append(xy[0]); y.append(xy[1])
    xy = np.array([x, y], dtype=np.float64)

    ab = xy.copy()
    ab[0] -= s; ab[1] -= t
    dist_ab = (ab[0]**2 + ab[1]**2) ** 0.5

    bc = xy.copy()
    bc[0] -= u; bc[1] -= v
    dist_bc = (bc[0]**2 + bc[1]**2) ** 0.5

    dist = dist_ab + dist_bc
    margin = V * T - dist
    margin.sort()
    if margin[-1] >= 0:
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
