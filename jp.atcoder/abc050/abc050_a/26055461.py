import typing



def main() -> typing.NoReturn:
  a, op, b = input().split()
  a, b = int(a), int(b)
  c = a + b if op == '+' else a - b
  print(c)


main()
