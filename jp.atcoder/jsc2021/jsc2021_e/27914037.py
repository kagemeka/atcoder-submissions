import typing


def main() -> typing.NoReturn:
    k = int(input())
    s = input()

    n = len(s)
    for _ in range(k):
        if n == 0:
            print('impossible')
            return
        n >>= 1

    if n == 1:
        print('impossible')
        return

    # n is initial length
    print(n)

    def dfs():
        ...
    # it's hard

main()
