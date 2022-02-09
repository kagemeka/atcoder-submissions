import typing


def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  c = 1
  c *= (h + 1) // 2
  c *= (w + 1) // 2
  print(c)


main()
