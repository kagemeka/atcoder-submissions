def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    mx = -1
    s1 = 0
    s2 = 0
    for i in range(n):
        mx = max(mx, a[i])
        s1 += a[i]
        s2 += s1
        print(mx * (i + 1) + s2)


if __name__ == "__main__":
    main()
