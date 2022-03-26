def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    b = [0] * (m + 1)

    for i in range(m, -1, -1):
        k = n + i
        assert c[k] % a[n] == 0
        q = c[k] // a[n]

        for j in range(n, -1, -1):
            c[j + i] -= q * a[j]
        b[i] = q
    print(*b)


if __name__ == "__main__":
    main()
