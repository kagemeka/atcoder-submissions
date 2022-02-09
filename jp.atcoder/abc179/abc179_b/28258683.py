import typing


def main() -> typing.NoReturn:
    n = int(input())

    cnt = 0
    flg = False
    for _ in range(n):
        d0, d1 = map(int, input().split())
        if d0 == d1:
            cnt += 1
        else:
            cnt = 0
        flg |= cnt >= 3
    print('Yes' if flg else 'No')

main()
