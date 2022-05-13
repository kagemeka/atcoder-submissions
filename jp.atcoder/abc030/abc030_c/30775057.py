def main() -> None:
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    i = j = 0
    t = 0
    count = 0
    while True:
        while i < n and a[i] < t:
            i += 1
        if i == n:
            break
        t = a[i] + x
        while j < m and b[j] < t:
            j += 1
        if j == m:
            break
        t = b[j] + y
        count += 1
    print(count)


if __name__ == '__main__':
    main()
