import typing



def main() -> typing.NoReturn:
  k, x = map(int, input().split())
  m = 10 ** 6
  s = range(max(x - k + 1, -m), min(x + k - 1, m) + 1)
  print(*s)


main()
