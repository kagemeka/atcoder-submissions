import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
graph = [None] * n
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if not a: continue
    graph[i] = np.array([sys.stdin.readline().split() for _ in range(a)], dtype=np.int16).T

def main():
    comb = (np.arange(1 << n)[:, None] >> np.arange(n) & 1).astype(np.bool)
    ok = np.full(1 << n, True, dtype=np.bool)
    for i in range(n):
        if graph[i] is None: continue
        x, y = graph[i]
        ok &= ~comb[:, i] | np.all(comb[:, x-1] == y.astype(np.bool), axis=1)

    print(np.amax(comb[ok].sum(axis=1)))

if __name__ ==  '__main__':
    main()
