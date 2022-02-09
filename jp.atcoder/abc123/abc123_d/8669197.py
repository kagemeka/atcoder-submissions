import sys
import numpy as np

INF = 10 ** 18

def main():
    x, y, z, K = map(int, sys.stdin.readline().split())
    abc = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = np.append(abc[:x], INF)
    b = np.append(abc[x:x + y], INF)
    c = np.append(abc[x + y:x + y+ z], INF)
    a = np.sort(a)[::-1]
    b = np.sort(b)[::-1]
    c = np.sort(c)[::-1]

    res = []
    for i in range(1, min(K, x) + 1):
        for j in range(1, min(y, K // i) + 1):
            for k in range(1, min(z, K // (i * j)) + 1):
                res.append(a[i] + b[j] + c[k])

    res = sorted(res, reverse=True)[:K]
    print('\n'.join(map(str, res)))

if __name__ == "__main__":
    main()
