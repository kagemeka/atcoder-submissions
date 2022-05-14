def main() -> None:
    n, w = map(int, input().split())
    a = list(map(int, input().split()))

    K = 1 << 22
    is_good = [False] * K

    for i in range(n):
        x = a[i]
        is_good[x] |= True
        for j in range(i + 1, n):
            y = x + a[j]
            is_good[y] |= True
            for k in range(j + 1, n):
                is_good[y + a[k]] |= True

    print(sum(is_good[1 : w + 1]))


if __name__ == "__main__":
    main()
