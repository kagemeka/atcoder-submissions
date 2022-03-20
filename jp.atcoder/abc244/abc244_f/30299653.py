def main() -> None:
    n, m = map(int, input().split())
    uv = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    g = [[] for _ in range(n)]
    for u, v in uv:
        g[u].append(v)
        g[v].append(u)

    remain = set(range(1 << n))
    # empty set's length is 0.

    consumed = [[False] * n for _ in range(1 << n)]
    remain.remove(0)
    current = set()
    for i in range(n):
        current.add((1 << i, i))
        consumed[1 << i][i] = True

    sum_length = 0
    length = 0
    while remain:
        length += 1
        nxt = set()
        for s, i in current:
            if s in remain:
                remain.remove(s)
                sum_length += length
            for j in g[i]:
                t = s ^ (1 << j)
                if consumed[t][j]:
                    continue
                nxt.add((t, j))
                consumed[t][j] = True
        current = nxt
    print(sum_length)


if __name__ == "__main__":
    main()
