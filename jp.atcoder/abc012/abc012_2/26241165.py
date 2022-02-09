import typing


def main() -> typing.NoReturn:
  n = int(input())

  h, n = divmod(n, 60 ** 2)
  m, s = divmod(n, 60)
  print(f'{h:02}:{m:02}:{s:02}')


main()
