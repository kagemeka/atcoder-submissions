import typing


def main() -> typing.NoReturn:
    n = int(input())

    # 1.08x >= n >= x
    # n >= x >= 100n // 108
    # brute-force

    for x in range(1, n + 1):
        if 108 * x // 100 != n: continue
        print(x)
        return
    print(':(')

main()
