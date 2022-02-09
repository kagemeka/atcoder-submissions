import typing


def main() -> typing.NoReturn:
    x, y, a, b = map(int, input().split())
    exp = 0
    while True:
        if x * a < x + b:
            if x * a >= y: break
            x *= a
            exp += 1
            continue
        exp += (y - 1 - x) // b
        break
    print(exp)

main()
