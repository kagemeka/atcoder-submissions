# 2019-11-24 20:59:47(JST)
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    m = map(int, sys.stdin.read().split())
    ab = list(zip(m, m))

    graph = [[] for _ in range(n + 1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)

    root = 1
    parent = [0] * (n + 1)
    order = []
    stack = [root]

    while stack:
        x = stack.pop()
        order.append(x)
        for y in graph[x]:
            if y == parent[x]:
                continue
            parent[y] = x
            stack.append(y)

    color = [-1] * (n + 1)
    for x in order:
        ng = color[x]
        c = 1
        for y in graph[x]:
            if y == parent[x]:
                continue
            if c == ng:
                c += 1
            color[y] = c
            c += 1

    res = []
    for a, b in ab:
        if parent[a] == b:
            res.append(color[a])
        else:
            res.append(color[b])

    print(max(res))
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()
