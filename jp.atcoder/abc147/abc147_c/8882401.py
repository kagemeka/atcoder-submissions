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

    res = np.full(2 ** n, 1, np.int64).reshape(-1, 1)
    comb = np.arange(2 ** n).reshape(-1, 1)
    for i in range(n):
        for x, y in xy[i]:
            bl = (comb >> i & 1) ^ (comb >> x & 1 ^ y)
            res &= bl

    cand = np.where(res == 1)[0]
    if not cand:
        return 0

    ans = np.amax(np.sum(cand.reshape(-1, 1) >> np.arange(n) & 1, axis=1))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
