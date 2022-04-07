def main() -> None:
    n, m = map(int, input().split())
    groups = [[] for _ in range(m)]
    for i in range(n):
        k, *l = map(int, input().split())
        for j in l:
            j -= 1
            groups[j].append(i)

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

    for members in groups:
        for i in range(len(members) - 1):
            u, v = members[i], members[i + 1]
            unite(u, v)
    print("YES" if len(set(find_root(i) for i in range(n))) == 1 else "NO")


if __name__ == "__main__":
    main()
