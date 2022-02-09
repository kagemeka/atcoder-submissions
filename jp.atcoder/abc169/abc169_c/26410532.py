import typing



def main() -> typing.NoReturn:
  a, b = input().split()
  a = int(a)
  b = int(float(b) * 100)
  print(a * b // 100)


main()
