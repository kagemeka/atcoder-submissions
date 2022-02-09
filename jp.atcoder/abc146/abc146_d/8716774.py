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

    root = 1
    q = deque()
    q.append(root)
    parent = [None] * (n + 1)
    color = [0] * (n + 1) # color[y]はx = parent[y]としてcolor[x] に依存する。
    print(color)
    while q:
        x = q.popleft()
        c = 1
        for y in G[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            if color[x] == c:
                c += 1
            color[y] = c
            q.append(y)

    k = max(color)
    print(k)
    print('\n'.join(map(str, color[2:])))

if __name__ == '__main__':
    main()
