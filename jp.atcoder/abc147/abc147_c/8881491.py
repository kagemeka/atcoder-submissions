import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
x = []
y = []
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    xy = [sys.stdin.readline().split() for _ in range(a)]
    if not xy:
        x.append(None)
        y.append(None)
        continue
    xi, yi = np.array(xy, np.int64).T
    x.append(xi-1)
    y.append(yi)

def main():

    ans = 0
    for comb in range(2 ** n):
        cnt = 0
        for i in range(n):
            if not comb >> i & 1:
                continue
            if x[i] is None:
                cnt += 1
                continue
            if np.count_nonzero(comb >> x[i] & 1 ^ y[i]):
                break
            cnt += 1
        else:
            ans = max(ans, cnt)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
