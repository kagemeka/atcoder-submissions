import sys

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
    stack = [0]
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if parent[y] is not None: continue
            parent[y] = x
            stack.append(y)

    if None in parent:
        print('No')
    else:
        print('Yes')
        for i in range(1, n):
            print(parent[i] + 1)

if __name__ == '__main__':
    main()
