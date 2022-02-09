import typing


def main() -> typing.NoReturn:
  a, b = map(int, input().split())
  print(pow(32, a - b))


main()
