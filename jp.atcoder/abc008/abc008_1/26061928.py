import typing


def main() -> typing.NoReturn:
  s, t = map(int, input().split())
  print(t - s + 1)


main()
