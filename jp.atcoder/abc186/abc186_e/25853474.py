import typing
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8), cache=True)
def ext_gcd(a: int, b: int) -> typing.Tuple[int, int, int]:
  if not b: return a, 1, 0
  g, s, t = ext_gcd(b, a % b)
  return g, t, s - a // b * t



@nb.njit((nb.i8, nb.i8), cache=True)
def mod_inv(a: int, mod: int) -> int:
  g, p, q = ext_gcd(a, mod)
  if g != 1:
    raise ArithmeticError(
      'modular multiplicative inverse does not exist.'
    )
  return p % mod



# @nb.njit((nb.i8[:], nb.i8[:], nb.i8), cache=True)
# def garner(
#   r: np.ndarray,
#   m: np.ndarray,
#   mod: int,
# ) -> int:
#   n = r.size
#   assert m.size == n
#   m = np.hstack((m, np.array([mod])))
#   s = np.zeros(n + 1, np.int64)
#   m_prod = np.full(n + 1, 1, np.int64)
#   for i in range(n):
#     t = (r[i] - s[i]) % m[i] * mod_inv(m_prod[i], m[i]) % m[i]
#     s[i + 1:] += t * m_prod[i + 1:] % m[i + 1:]
#     s %= m
#     m_prod = m_prod * m[i] % m
#   return s[-1], m_prod[-1]



@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def garner(
  r: np.ndarray,
  m: np.ndarray,
) -> int:
  n = r.size
  assert m.size == n
  x = 0
  m_prod = 1
  for i in range(n):
    t = (r[i] - x) * mod_inv(m_prod, m[i]) % m[i]
    x += t * m_prod
    m_prod *= m[i]
  return x



@nb.njit((nb.i8, ) * 3, cache=True)
def solve(n: int, s: int, k: int) -> typing.NoReturn:
  d, _, _ = ext_gcd(n, k)
  if s % d:
    print(-1)
    return
  n //= d
  k //= d
  s //= d
  r = np.array([0, s])
  m = np.array([n, k])
  y = garner(r, m)
  lcm = n * k * d
  y %= lcm
  if y < s: y += lcm
  print((y - s) // k)


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n, s, k = map(int, input().split())
    solve(n, s, k)

main()
