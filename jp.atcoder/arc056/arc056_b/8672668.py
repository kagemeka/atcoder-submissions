# 2019-11-27 17:10:30(JST)
import sys
def main():
    n, m, s = map(int, sys.stdin.readline().split())
    uv = map(int, sys.stdin.read().split())
    uv = list(zip(uv, uv))

    graph = [[] for _ in range(n+1)]
    for u, v in uv:
        graph[u].append(v)
        graph[v].append(u)

    res = []
    for i in range(1, s + 1):
        found = False
        if i == s:
            res.append(s)
            break
        stack = [s]
        checked = set()
        while stack:
            x = stack.pop()
            for y in graph[x]:
                if y == i:
                    res.append(y)
                    found = True
                    graph[i] = None
                    break
                if not graph[y]:
                    continue
                if not y in checked:
                    stack.append(y)
                    checked.add(y)
            if found:
                break

    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main()
