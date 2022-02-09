import typing


def main() -> typing.NoReturn:
  a = input()
  b = input()
  s = a if len(a) >= len(b) else b
  print(s)


main()
