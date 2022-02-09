import typing


def main() -> typing.NoReturn:
  a = int(input())
  b = int(input())
  c = (a + b - 1) // b * b
  print(c - a)


main()
