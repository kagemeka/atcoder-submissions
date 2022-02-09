import typing


def main() -> typing.NoReturn:
    print('Won' if len(set(input())) == 1 else 'Lost')


main()
