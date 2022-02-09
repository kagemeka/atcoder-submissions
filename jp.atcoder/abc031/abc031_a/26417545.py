import typing



def main() -> typing.NoReturn:
  a, d = map(int, input().split())
  print((a + 1) * d if a <= d else a * (d + 1))


main()
