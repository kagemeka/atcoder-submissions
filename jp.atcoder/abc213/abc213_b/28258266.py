import typing

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    idx = sorted(range(n), key=lambda i: a[i])
    print(idx[-2] + 1)

main()
