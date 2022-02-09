import typing



def main() -> typing.NoReturn:
  mod = 10 ** 9 + 7
  a, b, c = map(int, input().split())
  print(a * b % mod * c % mod)


main()
