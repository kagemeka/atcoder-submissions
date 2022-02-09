import typing




def main() -> typing.NoReturn:
  a = int(input())
  x = a // 2
  print(x * (a - x))


main()
