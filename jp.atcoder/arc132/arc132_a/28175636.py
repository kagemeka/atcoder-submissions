import typing


def main() -> typing.NoReturn:
    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    q = int(input())
    rc = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(q)]

    res = [''] * q
    for i, (y, x) in enumerate(rc):
        y, x = r[y], c[x]
        if x >= n - y + 1 and y >= n - x + 1:
            res[i] = '#'
        else:
            res[i] = '.'
    print(''.join(res))

main()
