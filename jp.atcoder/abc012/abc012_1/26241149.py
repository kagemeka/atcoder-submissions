import typing


def main() -> typing.NoReturn:
  print(*input().split()[::-1])


main()
