import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8), cache=True)
def ext_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
  if not b: return a, 1, 0
  g, s, t = ext_gcd(b, a % b)
  return g, t, s - a // b * t




@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def crt(
  r: np.ndarray,
  m: np.ndarray,
) -> typing.Tuple[int, int]:
  r0, m0 = 0, 1
  assert r.size == m.size
  for i in range(r.size):
    r1, m1 = r[i], m[i]
    d, p, q = ext_gcd(m0, m1)
    if (r1 - r0) % d: return 0, 0
    r0 += m0 * ((r1 - r0) // d * p % (m1 // d))
    m0 *= m1 // d
    r0 %= m0
  return r0, m0


@nb.njit((nb.i8, ) * 3, cache=True)
def solve(n: int, s: int, k: int) -> typing.NoReturn:
  r = np.array([0, s])
  m = np.array([n, k])
  y, m0 = crt(r, m)
  if m0 == 0:
    print(-1)
    return
  if y < s: y += m0
  print((y - s) // k)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, s, k = map(int, input().split())
    solve(n, s, k)

main()
