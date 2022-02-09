import typing

def main() -> typing.NoReturn:
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    p = 1
    MOD = 10 ** 9 + 7
    for i in range(n):
        p *= max(0, c[i] - i)
        p %= MOD
    print(p)

main()
