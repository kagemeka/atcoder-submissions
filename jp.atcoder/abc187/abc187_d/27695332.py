import typing

def main() -> typing.NoReturn:
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]


    ab.sort(key=lambda x: 2 * x[0] + x[1])
    s = sum(a for a, _ in ab)
    t = 0
    for i in range(n):
        a, b = ab[-1 - i]
        t += a + b
        s -= a
        if t > s:
            print(i + 1)
            return


main()
