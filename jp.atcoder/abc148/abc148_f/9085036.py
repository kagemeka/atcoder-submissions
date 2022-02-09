import sys

n, u, v, *ab = map(int, sys.stdin.read().split())
ab = list(zip(*[iter(ab)] * 2))
graph = [[] for _ in range(n+1)]
for a, b in ab:
    graph[a].append(b)
    graph[b].append(a)


def main():
    dist_u = [None] * (n + 1)
    dist_u[u] = 0
    stack = [u]

    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist_u[y] is None:
                dist_u[y] = dist_u[x] + 1
                stack.append(y)

    dist_v = [None] * (n + 1)
    dist_v[v] = 0
    stack = [v]
    contain_v = [False] * (n + 1)
    contain_v[v] = True
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist_v[y] is None:
                dist_v[y] = dist_v[x] + 1
                stack.append(y)

    d = 1
    for i in range(1, n+1):
        if dist_v[i] >= dist_u[i]:
            d = max(d, dist_v[i])
    ans = d - 1
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
