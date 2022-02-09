import typing



def main() -> typing.NoReturn:
  a, b = input().split()
  print(int(a + b) * 2)


main()
