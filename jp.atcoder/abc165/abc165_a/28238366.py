import typing



def main() -> typing.NoReturn:
    k = int(input())
    a, b = map(int, input().split())
    print('OK' if a <= b // k * k else 'NG')

main()
