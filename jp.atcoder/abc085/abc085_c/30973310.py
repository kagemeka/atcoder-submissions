def main() -> None:
    n, y = map(int, input().split())
    y //= 1000
    # 10i + 5j + k = y
    # i + j + k = n
    # 9i + 4j = y - n

    for i in range(n + 1):
        s = y - n - 9 * i
        if s < 0:
            break
        if s % 4 != 0:
            continue
        j = s // 4
        k = n - i - j
        if k < 0:
            continue
        print(i, j, k)
        return
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
