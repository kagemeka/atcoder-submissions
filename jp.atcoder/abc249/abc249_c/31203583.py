def main() -> None:
    n, k = map(int, input().split())
    K = 26

    strings = [set(input()) for _ in range(n)]
    a = [0] * n
    for i in range(n):
        for c in strings[i]:
            a[i] |= 1 << (ord(c) - ord("a"))

    mx = 0
    for s in range(1 << n):
        count = [0] * K
        for i in range(n):
            if ~s >> i & 1:
                continue
            for j in range(K):
                count[j] += a[i] >> j & 1
        mx = max(mx, sum(c == k for c in count))

    print(mx)


if __name__ == "__main__":
    main()
