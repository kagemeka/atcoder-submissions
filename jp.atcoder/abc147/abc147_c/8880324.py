import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
xy = [[] for _ in range(n)]

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    for j in range(a):
        x, y = map(int, sys.stdin.readline().split())
        xy[i].append((x-1, y))
xy = np.array(xy)
x, y = xy[:, :].T
x = x.T
y = y.T

def main():
    ans = 0
    for comb in range(2 ** n):
        cnt = 0
        for i in range(n):
            if not comb >> i & 1:
                continue
            if np.any(comb >> x[i] & 1 ^ y[i]):
                break
            cnt += 1
        else:
            ans = max(ans, cnt)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
