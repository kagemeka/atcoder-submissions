import typing


def main() -> typing.NoReturn:
    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q = int(input())
    rc = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]


    res = [''] * q
    for i, (y, x) in sorted(enumerate(rc), key=lambda x: -max(r[x[1][0]], c[x[1][1]])):
        if r[y] > 0 and c[x] > 0:
            res[i] = '#'
            r[y] -= 1
            c[x] -= 1
        else:
            res[i] = '.'
    print(''.join(res))


main()
