import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def mod_matrix_dot(
  a: np.ndarray,
  b: np.ndarray,
  mod: int,
) -> np.ndarray:
  ha, wa = a.shape
  hb, wb = b.shape
  assert wa == hb
  c = np.zeros((ha, wb), np.int64)
  for i in range(ha):
    for j in range(wb):
      c[i, j] = np.sum(a[i] * b[:, j] % mod) % mod
  return c



@nb.njit
def mod_matrix_pow(
  a: np.ndarray,
  n: int,
  mod: int,
) -> np.ndarray:
  m = len(a)
  assert a.shape == (m, m)
  x = np.eye(m, dtype=np.int64)
  while n:
    if n & 1:
      x = mod_matrix_dot(x, a, mod)
    a = mod_matrix_dot(a, a, mod)
    n >>= 1
  return x


@nb.njit
def mod_pow(
  x: int,
  n: int,
  mod: int,
) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit(
  (nb.i8[:, :], nb.i8[:], nb.i8[:], nb.i8),
  cache=True,
)
def solve(
  a: np.ndarray,
  x: np.ndarray,
  y: np.ndarray,
  k: int,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  n = a.size
  m = x.size

  inv_2 = mod_pow(2, mod - 2, mod)
  inv_m = mod_pow(m, mod - 2, mod)

  def make_graph():
    g = np.zeros((n, n), np.int64)
    for i in range(m):
      g[x[i], y[i]] = g[y[i], x[i]] = 1
    for i in range(n):
      c = g[i].sum()
      g[i] *= inv_2
      g[i, i] = m - c * inv_2
    g = g % mod * inv_m % mod
    return g

  g = make_graph()
  g = mod_matrix_pow(g, k, mod)
  res = mod_matrix_dot(g, a, mod)
  return res.ravel()


def main() -> typing.NoReturn:
  n, m, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  a = a[:, None]
  x, y = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2).T - 1
  res = solve(a, x, y, k)
  print(*res, sep='\n')


main()
