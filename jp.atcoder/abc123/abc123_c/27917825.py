import typing
import sys

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, sys.stdin.read().split()))
    mn = min(a)
    s = (n + mn - 1) // mn + 4
    print(s)

main()
