import typing


def main() -> typing.NoReturn:
  a, b = map(
    int,
    input().split(),
  )
  c = (a - b) / 3 + b
  print(c)

main()
