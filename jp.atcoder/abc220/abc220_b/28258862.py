import typing



def main() -> typing.NoReturn:
    k = int(input())

    def to_decimal(base: int, digits: typing.List[int]) -> int:
        a = 1
        n = 0
        for d in digits:
            n += a * d
            a *= base
        return n


    a, b = input().split()
    a = to_decimal(k, list(map(int, a))[::-1])
    b = to_decimal(k, list(map(int, b))[::-1])
    print(a * b)

main()
