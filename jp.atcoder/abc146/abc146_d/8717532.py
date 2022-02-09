import sys
from collections import deque

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = map(int, sys.stdin.read().split())
    ab = list(zip(ab, ab))

    G = [[] for _ in range(n + 1)]
    for a, b in ab:
        G[a].append(b)
        G[b].append(a)

    q = deque([1]) # root = 1
    parent = [None] * (n + 1)
    color = [0] * (n + 1) # color of the edge(parent[y], y)

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

    print(max(color))

    for a, b in ab:
        if a == parent[b]:
            print(color[b])
        else:
            print(color[a])

if __name__ == '__main__':
    main()
