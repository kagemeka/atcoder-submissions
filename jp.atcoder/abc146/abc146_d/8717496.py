import sys
from collections import deque
import numpy as np

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2)

    G = [[] for _ in range(n + 1)]
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)

    parent = np.zeros(n + 1, dtype=np.int64)
    color = np.zeros(n + 1, dtype=np.int64) # color of the edge(parent[y], y)

    q = deque([1]) # root = 1
    while q:
        x = q.popleft()
        ng = color[x]
        c = 1
        for y in G[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            if c == ng:
                c += 1
            color[y] = c
            q.append(y)
            c += 1

    print(np.amax(color))

    for a, b in ab:
        if a == parent[b]:
            print(color[b])
        else:
            print(color[a])

if __name__ == '__main__':
    main()
