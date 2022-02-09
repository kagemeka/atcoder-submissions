import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
graph = [None] * n
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if not a: continue
    graph[i] = np.array([sys.stdin.readline().split() for _ in range(a)], dtype=np.int16).T

def main():
    comb = np.arange(1 << n)[:, None] >> np.arange(n) & 1
    ok = np.full(1 << n, True)
    for i in range(n):
        if graph[i] is None: continue
        x, y = graph[i]
        bl = (comb[:, i] ^ 1) | np.all(comb[:, x-1] == y, axis=1)
        ok &= bl
    print(np.amax(comb[ok].sum(axis=1)))

if __name__ ==  '__main__':
    main()
