import typing


def gcd(a: int, b: int) -> int: return gcd(b, a % b) if b else a

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    g = 0
    for x in a:
        g = gcd(g, x)
    print(g)

main()
