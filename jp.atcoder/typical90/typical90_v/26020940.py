import typing
import math

def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  g = math.gcd(*a)
  cnt = sum(x // g - 1 for x in a)
  print(cnt)

main()
