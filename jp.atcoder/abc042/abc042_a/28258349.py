import typing

def main() -> typing.NoReturn:
    a = list(map(int, input().split()))
    a.sort()
    print('YES' if a[0] == a[1] == 5 and a[2] == 7 else 'NO')

main()
