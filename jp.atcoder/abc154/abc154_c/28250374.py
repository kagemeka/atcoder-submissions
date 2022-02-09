import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    print('YES' if len(set(a)) == n else 'NO')

main()
