import typing


def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 1
    x -= 1
    known_by = [False] * n
    known_by[x] = True
    while True:
        x = a[x] - 1
        if known_by[x]: break
        known_by[x] = True
        cnt += 1
    print(cnt)


main()
