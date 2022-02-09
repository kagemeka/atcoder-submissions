import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
sx, sy, gx, gy, T, V, n = I[:7]
xy = I[7:].reshape(-1, 2)

def dist(s, g):
    return np.sqrt(np.sum(np.power(g - s, 2), axis=1))

def main():
    d = dist([sx, sy], xy) + dist(xy, [gx, gy])

    if np.any(d <= V * T):
        ans = 'YES'
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
