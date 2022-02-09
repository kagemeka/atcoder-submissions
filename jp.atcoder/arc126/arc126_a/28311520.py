import typing


def solve() -> typing.NoReturn:
    a, b, c = map(int, input().split())
    # 3, 3, 4
    # 3, 3, 2, 2
    # 4, 4, 2
    # 4, 2, 2, 2
    # 2, 2, 2, 2, 2

    cnt = 0
    # b //= 2
    tmp = min(b // 2, c)
    if b // 2 >= c:
        cnt += c
        b -= 2 * c
        tmp = min(b // 2, a // 2)
        cnt += tmp
        a -= tmp * 2
    else:
        cnt += b // 2
        c -= b // 2
        tmp = min(a, c // 2)
        cnt += tmp
        a -= tmp
        c -= tmp * 2
        tmp = min(a // 3, c)
        cnt += tmp
        a -= 3 * tmp
        c -= tmp
    cnt += a // 5
    print(cnt)


def main() -> typing.NoReturn:
    t = int(input())
    for _ in range(t):
        solve()


main()
