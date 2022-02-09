import typing


def main() -> typing.NoReturn:
    # BFS Tree
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)


    parent = [-1] * n
    que = [0]
    for u in que:
        for v in g[u]:
            if v == parent[u]: continue
            if parent[v] != -1: continue
            parent[v] = u
            que.append(v)

    if parent.count(-1) >= 2:
        print('No')
    else:
        print('Yes')

    for i in range(1, n):
        print(parent[i] + 1)


main()
