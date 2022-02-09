import typing


def main() -> typing.NoReturn:
    # s = a + b
    # t = c + d
    # s - t = k
    # fix s

    n, k = map(int, input().split())
    cnt = 0
    for s in range(2, 2 * n + 1):
        t = s - k
        cnt += max(0, min(s - 1, n) - max(1, s - n) + 1) * max(0, min(t - 1, n) - max(1, t - n) + 1)

    print(cnt)

main()
