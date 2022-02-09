import typing
import math

def main() -> typing.NoReturn:
  *a, = map(int, input().split())
  g = 0
  for x in a:
    g = math.gcd(g, x)
  cnt = sum(x // g - 1 for x in a)
  print(cnt)

main()
