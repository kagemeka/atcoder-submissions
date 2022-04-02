def main() -> None:
    n, k, x = map(int, input().split())

    a = list(map(int, input().split()))
    # s = sum(a)
    for i in range(n):
        q, r = divmod(a[i], x)
        if q <= k:
            a[i] = r
            k -= q
        else:
            a[i] -= k * x
            k = 0
            break
    a.sort(reverse=True)
    for i in range(min(n, k)):
        a[i] = 0
    print(sum(a))


if __name__ == "__main__":
    main()
