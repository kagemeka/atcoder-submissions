import typing
import sys
from math import gcd


def solve(
  ab: int,
) -> typing.NoReturn:

  s = {(0, 0)}
  g = 0
  for a, b in ab:
    ns = set()
    for gx, gy in s:
      ns.add((
        gcd(gx, a),
        gcd(gy, b),
      ))
      ns.add((
        gcd(gx, b),
        gcd(gy, a),
      ))
    s = ns
    g = gcd(g, a, b)

  mx = 0
  for gx, gy in s:
    mx = max(mx, gx * gy)
  print(mx // g)



def main() -> typing.NoReturn:
  n = int(input())
  ab = map(
    int,
    sys.stdin.read().split(),
  )
  ab = zip(*[ab] * 2)
  solve(ab)


main()
