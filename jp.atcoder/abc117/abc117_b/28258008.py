import typing


def main() -> typing.NoReturn:
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    mx = max(l)
    print('Yes' if mx < s - mx else 'No')

main()
