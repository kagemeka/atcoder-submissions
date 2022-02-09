import typing

def gcd(a: int, b: int) -> int: return gcd(b, a % b) if b else a

def main() -> typing.NoReturn:
    a, b, c = map(int, input().split())
    print('YES' if c % gcd(a, b) == 0 else 'NO')

main()
