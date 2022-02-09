import typing


def main() -> typing.NoReturn:
  a, b, c = map(int, input().split())
  ok = a < pow(c, b)
  print('Yes' if ok else 'No')


main()
