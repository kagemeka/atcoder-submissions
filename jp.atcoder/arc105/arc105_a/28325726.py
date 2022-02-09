import typing


def main() -> typing.NoReturn:
    a = list(map(int, input().split()))
    n = 4
    s = sum(a)
    if s & 1:
        print('No')
        return
    s //= 2
    for t in range(1 << n):
        if sum(a[i] for i in range(n) if t >> i & 1) == s:
            print('Yes')
            return
    print('No')

main()
