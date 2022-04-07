def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    s = sum(a[: n - k + 1])
    count = 1
    for i in range(n - k + 1, n):
        if s // count <= a[i]:
            print(s // count)
            return
        s += a[i]
        count += 1
    print(s // count)


if __name__ == "__main__":
    main()
