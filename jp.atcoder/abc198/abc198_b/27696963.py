import typing



def main() -> typing.NoReturn:
    n = int(input())
    while n and n % 10 == 0:
        n //= 10
    n = str(n)
    print('Yes' if n == n[::-1] else 'No')


main()
