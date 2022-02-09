import typing


def main() -> typing.NoReturn:
    l, r = map(int, input().split())
    K = 2019
    if r // K * K >= l:
        print(0)
        return


    mn = K - 1
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            mn = min(mn, i * j % K)
    print(mn)

main()
