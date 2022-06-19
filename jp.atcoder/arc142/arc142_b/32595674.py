# mypy: ignore-errors


def main() -> None:
    n = int(input())

    # odd, even

    a = [[0] * n for _ in range(n)]

    h = (n - 1) >> 1
    for i in range(n):

        row = [i * n + (j + 1) for j in range(n)]
        a[i][::2] = row[: h + 1]
        a[i][1::2] = row[h + 1 :]
    for row in a:
        print(*row)


main()
