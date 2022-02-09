import sys
from collections import deque
import numpy as np

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = np.array(sys.stdin.read().split(), dtype=np.int32).reshape(-1, 2)

    G = [[] for _ in range(n + 1)]
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)

    parent = np.zeros(n + 1, dtype=np.int32)
    color = np.zeros((n + 1, n + 1), dtype=np.int32)
    root = 1
    ng = None
    q = deque()
    q.append((root, ng))

    while q:
        x, ng = q.popleft()
        c = 1
        for y in G[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            if c == ng:
                c += 1
            color[x][y] = c
            color[y][x] = c
            q.append((y, c))
            c += 1

    print(np.amax(color))
    for a, b in ab:
        print(color[a][b])

if __name__ == '__main__':
    main()
