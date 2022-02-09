import typing



def main() -> typing.NoReturn:
  a, b, c, k = map(int, input().split())
  s, t = map(int, input().split())
  cost = s * a + t * b - (s + t >= k) * (s + t) * c
  print(cost)


main()
