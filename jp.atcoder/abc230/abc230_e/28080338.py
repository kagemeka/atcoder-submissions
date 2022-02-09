import typing




def floor_sum(n: int) -> int:
    s = 0
    i = 1
    while i <= n:
        x = n // i
        j = n // x + 1
        s += x * (j - i)
        i = j
    return s

def main() -> typing.NoReturn:
    n = int(input())
    print(floor_sum(n))

main()
