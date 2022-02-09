import typing


def main() -> typing.NoReturn:
    n, a, b = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    d = max(arr) - min(arr)

    if d == 0:
        if b != 0:
            print(-1)
            return

        p = 1
    else:
        p = b / d
    arr = [p * x for x in arr]
    avg = sum(arr) / n
    q = a - avg
    print(p, q)


main()
