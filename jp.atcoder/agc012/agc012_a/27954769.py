import typing

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = sum(a[n::2])
    print(s)

main()
