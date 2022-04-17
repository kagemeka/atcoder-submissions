def main() -> None:
    n = int(input())
    a = [0] + list(map(int, input().split()))

    v = [0] * (n + 1)
    for i in range(n, 0, -1):
        for j in range(i * 2, n + 1, i):
            v[i] ^= v[j]
        v[i] ^= a[i]

    print(sum(v))
    print(*(i for i in range(1, n + 1) if v[i] == 1))


if __name__ == "__main__":
    main()
