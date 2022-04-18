def main() -> None:
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    v = [s[r + 1] - s[l] for l in range(n) for r in range(l, n)]
    K = 40

    res = 0
    for i in range(K, -1, -1):
        b = [x for x in v if x >> i & 1]
        if len(b) < k:
            continue
        v = b
        res |= 1 << i
    print(res)


if __name__ == "__main__":
    main()
