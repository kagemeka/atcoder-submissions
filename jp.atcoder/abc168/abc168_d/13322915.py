import sys
from collections import deque

n, m, *ab = map(int, sys.stdin.read().split())
ab = zip(*[iter(ab)] * 2)
graph = [[] for _ in range(n)]
for a, b in ab:
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

def main():
    parent = [None] * n
    parent[0] = 0
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if parent[y] is not None: continue
            parent[y] = x
            queue.append(y)

    if None in parent:
        print('No')
    else:
        print('Yes')
        for i in range(1, n):
            print(parent[i] + 1)

if __name__ == '__main__':
    main()
