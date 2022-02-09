import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
graph = [None] * n
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    graph[i] = np.array([[sys.stdin.readline().split()] for _ in range(a)], dtype=np.int8).T

def main():
    comb = np.arange(1 << n)[:, None] >> np.arange(n) & 1
    for i in range(n):
        x, y = graph[i]
        bl = (comb[:, i][:, None] ^ 1) | (comb[:, x-1] == y).reshape(len(comb), -1)
        bl = np.all(bl, axis=1)
        comb = comb[bl]
    print(np.amax(comb.sum(axis=1)))

if __name__ ==  '__main__':
    main()
