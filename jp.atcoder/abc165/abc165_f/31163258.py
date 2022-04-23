import bisect


def main() -> None:
    n = int(input())
    # memolize what the value has been excahnged with each value on node.
    # and retrive the original LIS at returning time.
    a = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    INF = 1 << 60
    original = [(-1, -1)] * n
    lis = [INF] * n

    length = [-1] * n
    stack = [0]
    parent = [-1] * n
    while stack:
        u = stack.pop()
        if u < 0:
            i, v = original[~u]
            lis[i] = v
            continue
        stack.append(~u)
        i = bisect.bisect_left(lis, a[u])
        original[u] = (i, lis[i])
        lis[i] = a[u]
        length[u] = bisect.bisect_left(lis, INF)
        for v in g[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    print(*length, sep='\n')


if __name__ == "__main__":
    main()
