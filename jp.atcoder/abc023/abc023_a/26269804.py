import typing


def main() -> typing.NoReturn:
  x = int(input())
  print(sum(divmod(x, 10)))


main()
