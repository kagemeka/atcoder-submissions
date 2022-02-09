import typing


def main() -> typing.NoReturn:
  x, y = map(int, input().split())
  print(y // x)


main()
