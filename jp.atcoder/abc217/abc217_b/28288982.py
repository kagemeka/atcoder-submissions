import typing


def main() -> typing.NoReturn:
    cand = {'ABC', 'ARC', 'AGC', 'AHC'}
    for _ in range(3):
        s = input()
        cand.remove(s)
    print(cand.pop())

main()
