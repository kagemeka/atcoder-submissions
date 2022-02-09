import typing


def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  print(min(a))


main()
