def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    indices = sorted(range(n), key=lambda i: -a[i])

    inf = 1 << 60
    mn = inf

    bigger_index = n
    for i in indices:
        if i < k:
            if bigger_index == n:
                continue
            mn = min(mn, k - i + bigger_index - k)
        else:
            bigger_index = min(bigger_index, i)
    print(-1 if mn == inf else mn)


if __name__ == "__main__":
    main()
