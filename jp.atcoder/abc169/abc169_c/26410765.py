import typing



def main() -> typing.NoReturn:
  a, b = input().split()
  a = int(a)
  b1, b0 = map(int, b.split('.'))
  print(a * (100 * b1 + b0) // 100)


main()
