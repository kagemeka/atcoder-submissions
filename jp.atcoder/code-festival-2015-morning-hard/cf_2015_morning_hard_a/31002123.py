def main() -> None:
    # greedy

    n = int(input())
    a = list(map(int, input().split()))

    l, r = 0, n - 1
    count = 0
    while l < r:
        assert r - l >= 2
        if a[l] * 2 + a[l + 1] <= a[r] * 2 + a[r - 1]:
            a[l + 2] += a[l] + a[l + 1] + 2
            count += a[l] * 2 + a[l + 1] + 1
            l += 2
        else:
            a[r - 2] += a[r] + a[r - 1] + 2
            count += a[r] * 2 + a[r - 1] + 1
            r -= 2
    print(count)


if __name__ == "__main__":
    main()
