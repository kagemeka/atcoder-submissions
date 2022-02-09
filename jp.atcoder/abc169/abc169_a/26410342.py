import typing


def main() -> typing.NoReturn:
  a, b = map(int, input().split())
  print(a * b)


main()
