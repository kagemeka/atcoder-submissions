import typing

# def base_convert_to_ten(base: int, digits: typing.Iterable[int]) -> int:

#     ...


def base_convert_from_ten(base: int, n: int) -> typing.List[int]:
    assert abs(base) >= 2
    if n == 0: return [0]
    digits = []
    while n:
        n, r = divmod(n, base)
        if r < 0:
            r -= base
            n += 1
        digits.append(r)
    return digits[::-1]

def main() -> typing.NoReturn:
    n = int(input())
    res = base_convert_from_ten(-2, n)
    print(''.join(map(str, res)))


main()
