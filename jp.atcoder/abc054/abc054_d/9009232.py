import sys
import numpy as np
from copy import deepcopy

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, ma, mb = I[:3]
a, b, c = I[3:].reshape(n, 3).T

def main():
    sa = np.sum(a)
    sb = np.sum(b)

    res = [[[[0, 0] for _ in range(sb+1)] for _ in range(sb + 1)] for _ in range(n+1)]
    res[0][0][0][0] = 1
    for i in range(n):
        res[i+1] = deepcopy(res[i])
        for j in range(sa+1):
            for k in range(sb+1):
                if j >= a[i] and k >= b[i]:
                    prev =  res[i][j-a[i]][k-b[i]]
                    if prev[0]:
                        res[i+1][j][k][0] = 1
                        if res[i+1][j][k][1]:
                            res[i+1][j][k][1] = min(prev[1] + c[i], res[i+1][j][k][1])
                        else:
                            res[i+1][j][k][1] = prev[1] + c[i]

    for i in range(1, min(sa//ma, sb//mb)+1):
        x = res[n][ma * i][mb * i]
        if x[0]:
            return x[1]
    return -1

if __name__ == '__main__':
    ans = main()
    print(ans)
