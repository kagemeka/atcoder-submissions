import typing


def main() -> typing.NoReturn:
    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q = int(input())
    rc = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]


    res = []
    for y, x in rc:
        if r[y] > 0 and c[x] > 0:
            res.append('#')
            r[y] -= 1
            c[x] -= 1
        else:
            res.append('.')
    print(''.join(res))


main()
