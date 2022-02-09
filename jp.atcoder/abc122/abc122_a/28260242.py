import typing


def main() -> typing.NoReturn:
    b = input()

    pair = dict(zip('ATCG', 'TAGC'))
    print(pair[b])

main()
