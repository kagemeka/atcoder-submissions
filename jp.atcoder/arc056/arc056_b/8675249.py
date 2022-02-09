# 2019-11-27 17:10:30(JST)
import sys
def main():
    n, m, s = map(int, sys.stdin.readline().split())
    uv = map(int, sys.stdin.read().split())
    uv = list(zip(uv, uv))

    graph = [[] for _ in range(n+1)]
    for u, v in uv:
        if u > v:
            graph[v].append(u)
        else:
            graph[u].append(v)

    res = []
    for i in range(1, s):
        if graph[i]:
            res.append(i)
    res.append(s)

    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main()
