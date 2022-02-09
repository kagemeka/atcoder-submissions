import typing



def main() -> typing.NoReturn:
  n, m = map(int, input().split())

  long = 6 * m
  short = n % 12 * 30+ m / 2
  delta = abs(long - short)
  print(min(delta, 360 - delta))


main()
