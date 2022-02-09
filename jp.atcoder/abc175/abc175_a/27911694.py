import typing


def main() -> typing.NoReturn:
    s = input()
    mx = 0
    for i in range(1, 4):
        if 'R' * i in s: mx = max(mx, i)
    print(mx)

main()
