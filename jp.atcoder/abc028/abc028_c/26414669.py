import typing




def main() -> typing.NoReturn:
  a, b, c, d, e = map(int, input().split())
  print(max(a + d + e, b + c + e))


main()
