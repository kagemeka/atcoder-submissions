def main() -> None:
    n, q = map(int, input().split())

    # b_i = a_i - a_{i - 1}
    # b_0 = 0
    # sum[l, r] is known
    # -> b_r - b_{l - 1} is known
    # -> we can move node_{l - 1} to node_r, vice-versa.
    # -> can we move node_0 to node_n?
    # connectivity
    # union find
    data = [-1] * (n + 1)

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

    for _ in range(q):
        l, r = map(int, input().split())
        unite(l - 1, r)

    print("Yes" if find_root(0) == find_root(n) else "No")


if __name__ == "__main__":
    main()
