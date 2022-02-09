import sys
import numpy as np

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, a, b, m = I[:4]
a -= 1; b -= 1
x, y = I[4:].reshape(-1, 2).T
G = np.zeros((n, n), dtype=np.int64)
G[x-1, y-1] = G[y-1, x-1] = 1

def main():
    vec = np.zeros(n, dtype=np.int64).reshape(-1, 1)
    vec[a, 0] = 1
    while vec[b, 0] == 0:
        vec = np.dot(G,vec)
        vec %= MOD

    return vec[b, 0]

if __name__ == '__main__':
    ans = main()
    print(ans)
