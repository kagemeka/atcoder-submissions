import typing


def main() -> typing.NoReturn:
    n = int(input())

    s = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0: continue
        s += i
    print(s)

main()
