import typing


def main() -> typing.NoReturn:
  a = int(input())
  b = int(input())
  d = abs(b - a)
  print(min(d, 10 - d))

main()
