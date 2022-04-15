def main() -> None:
    n, y = map(int, input().split())
    y //= 1000

    for i in range(n + 1):
        if 10 * i > y:
            break
        for j in range(n - i + 1):
            k = y - 10 * i - 5 * j
            s = i + j + k
            if s < n:
                break
            if s > n:
                continue
            print(i, j, k)
            return
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
