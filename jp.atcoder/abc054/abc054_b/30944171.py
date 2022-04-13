def main() -> None:
    n, m = map(int, input().split())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(m)]

    def is_same(y: int, x: int) -> bool:
        for i in range(m):
            for j in range(m):
                if a[y + i][x + j] == b[i][j]:
                    continue
                return False
        return True

    for y in range(n - m + 1):
        for x in range(n - m + 1):
            if is_same(y, x):
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
