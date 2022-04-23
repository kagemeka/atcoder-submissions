def main() -> None:
    # constrains for n kinds of ranges -> consider n-dimensional plane.
    n, m, q = map(int, input().split())

    # p <= l and r <= q -> add 1 to (y, x) satisfying y <= l and r <= x.
    # 2D imos method.

    K = 1 << 9

    s = [[0] * K for _ in range(K)]
    for _ in range(m):
        l, r = map(int, input().split())
        s[l][r] += 1

    for i in range(K):
        for j in range(K - 1):
            s[i][j + 1] += s[i][j]
    for j in range(K):
        for i in range(K - 1):
            s[i + 1][j] += s[i][j]

    pq = [tuple(map(int, input().split())) for _ in range(q)]
    for p, q in pq:
        print(s[-1][q] - s[p - 1][q])


if __name__ == "__main__":
    main()
