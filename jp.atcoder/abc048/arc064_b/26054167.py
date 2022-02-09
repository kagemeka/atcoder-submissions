import typing



def main() -> typing.NoReturn:
  a, b, x = map(int, input().split())

  def f(n):
    return n // x + 1

  print(f(b) - f(a - 1))


main()
