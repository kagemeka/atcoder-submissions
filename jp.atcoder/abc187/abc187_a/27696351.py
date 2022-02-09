import typing


def main() -> typing.NoReturn:
    def s(n: int) -> int:
        v = 0
        while n:
            v += n % 10
            n //= 10
        return v

    a, b = map(int, input().split())
    print(max(s(a), s(b)))


main()
