import sys
import numpy as np

n, d, *x = map(int, sys.stdin.read().split())
x = np.array(x, dtype=np.int64).reshape(n, d)

def main():
    cnt = 0
    for i in range(n-1):
        for j in range(i+1, n):
            dist = np.sqrt(((x[i] - x[j]) ** 2).sum())
            if dist == int(dist):
                cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
