import typing


def main() -> typing.NoReturn:
  a, b = input().split()
  print('H' if a == b else 'D')


main()
