import typing
import sys



def gcd(
  *ints: typing.Tuple[int],
) -> int:
  n = len(ints)
  if n == 0: return 0
  a = ints[-1]
  if n != 2:
    return gcd(
      a,
      gcd(*ints[:-1]),
    )
  b = ints[0]
  if not a: return b
  return gcd(a, b % a)


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
