def main() -> None:
    n, m = map(int, input().split())
    # reverse order
    # constructing graph

    edge = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)

    data = [-1] * n

    def find_root(u: int) -> int:
        if data[u] < 0:
            return u
        data[u] = find_root(data[u])
        return data[u]

    def unite(u: int, v: int) -> None:
        u, v = find_root(u), find_root(v)
        if u == v:
            return
        if data[u] > data[v]:
            u, v = v, u
        data[u] += data[v]
        data[v] = u

    result = [0] * n
    for i in range(n - 1, 0, -1):
        result[i - 1] = result[i] + 1
        for j in edge[i]:
            if j < i:
                continue
            if find_root(i) != find_root(j):
                unite(i, j)
                result[i - 1] -= 1
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
