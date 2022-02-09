import typing

def find_divisors(n: int) -> typing.List[int]:
    divs = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i != 0: continue
        divs.append(i)
        if n // i != i: divs.append(n // i)
    divs.sort()
    return divs


def main() -> typing.NoReturn:
    n = int(input())

    print(*find_divisors(n), sep='\n')


main()
