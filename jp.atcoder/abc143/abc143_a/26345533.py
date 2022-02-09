import typing


def main() -> typing.NoReturn:
  a, b = map(int, input().split())
  print(max(0, a - 2 * b))


main()
