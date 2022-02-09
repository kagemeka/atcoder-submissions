import typing
import sys
import math


def solve(n: int, s: int, k: int) -> typing.NoReturn:
  g = math.gcd(n, k)
  if s % g:
    print(-1)
    return
  s //= g
  k //= g
  n //= g
  x = pow(k, -1, n)
  c = -s * x % n
  print(c)



def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, s, k = map(int, input().split())
    solve(n, s, k)

main()
