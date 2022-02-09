import typing


def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    # greedy

    res = []
    for i in range(h):
        for j in range(w - 1):
            if a[i][j] & 1 == 0: continue
            a[i][j + 1] += 1
            a[i][j] -= 1
            res.append((i, j, i + 1, j))

    for i in range(h - 1):
        if a[i][w - 1] & 1 == 0: continue
        a[i + 1][w - 1] += 1
        a[i][w - 1] -= 1
        res.append((i, w - 1, i + 1, w - 1))

    print(len(res))
    for row in res:
        print(*map(lambda x: x + 1, row))

main()
