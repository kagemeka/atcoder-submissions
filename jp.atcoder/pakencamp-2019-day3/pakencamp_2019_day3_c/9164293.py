import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
a = I[2:].reshape(n, m)

def main():
    res = 0
    for i in range(m-1):
        for j in range(i+1, m):
            total_score = np.maximum(a[:, i], a[:, j]).sum()
            res = max(res, total_score)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
