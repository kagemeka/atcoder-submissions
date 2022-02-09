import sys
import numpy as np

h, w = map(int, sys.stdin.readline().split())
s = np.array([list(sys.stdin.readline().rstrip()) for _ in range(h)], dtype='U')
s = np.pad(s, 1)

def main():
    l = np.zeros((h+2, w+2), dtype=np.int64)
    r = np.zeros((h+2, w+2), dtype=np.int64)
    u = np.zeros((h+2, w+2), dtype=np.int64)
    d = np.zeros((h+2, w+2), dtype=np.int64)

    for i in range(1, w+1):
        bl = s[:, i] == '#'
        l[~bl, i] = l[~bl, i-1] + 1
        i = w+1-i
        bl = s[:, i] == '#'
        r[~bl, i] = r[~bl, i+1] + 1

    for i in range(1, h+1):
        bl = s[i, :] == '#'
        u[i, ~bl] = u[i-1, ~bl] + 1
        i = h+1-i
        bl = s[i, :] == '#'
        d[i, ~bl] = d[i+1, ~bl] + 1

    res = l + r + u + d - 3
    return np.amax(res[1:h+1, 1:w+1])

if __name__ == '__main__':
    ans = main()
    print(ans)
