import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
xy = [[] for _ in range(n)]
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    for _ in range(a):
        x, y = map(int, sys.stdin.readline().split())
        xy[i].append((x - 1, y))

def main():
    comb = (np.arange(2 ** n).reshape(-1, 1) >> np.arange(n) & 1).astype(np.bool)
    for i in range(n):
        for x, y in xy[i]:
            bl = ~comb[:, i] | (comb[:, x] == np.bool(y))
            comb = comb[bl]

    ans = np.amax(np.sum(comb, axis=1))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
