import typing
import sys
import numpy as np
import numba as nb

MOD = 998_244_353



S = typing.TypeVar('S')
@nb.njit
def fw_build(
  op: typing.Callable[[S, S], S],
  a: np.ndarray,
) -> np.ndarray:
  n = len(a)
  fw = np.empty((n + 1, ) + a.shape[1:], np.int64)
  fw[1:] = a.copy()
  for i in range(1, n + 1):
    j = i + (i & -i)
    if j < n + 1: fw[j] = op(fw[j], fw[i])
  return fw


@nb.njit
def fw_set(
  op: typing.Callable[[S, S], S],
  fw: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  assert 0 <= i < len(fw) - 1
  i += 1
  while i < len(fw):
    fw[i] = op(fw[i], x)
    i += i & -i


@nb.njit
def fw_get(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  fw: np.ndarray,
  i: int,
) -> S:
  assert 0 <= i < len(fw)
  v = e()
  while i > 0:
    v = op(v, fw[i])
    i -= i & -i
  return v


S = typing.TypeVar('S')
@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
  return fw_get(fw_op, fw_e, fw, i)


@nb.njit
def set_fw(fw: np.ndarray, i: int, x: S) -> typing.NoReturn:
  fw_set(fw_op, fw, i, x)


@nb.njit
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
  return fw_op(
    fw_inverse(fw_get(fw_op, fw_e, fw, l)),
    fw_get(fw_op, fw_e, fw, r),
  )


@nb.njit
def fw_inverse(a: S) -> S: return -a % MOD


@nb.njit
def fw_op(a: S, b: S) -> S: return (a + b) % MOD


@nb.njit
def fw_e() -> S: return 0


@nb.njit
def mod_pow(x: int, n: int, mod: int) -> int:
  y = 1
  while n:
    if n & 1: y = y * x % mod
    x = x * x % mod
    n >>= 1
  return y


@nb.njit
def mod_inverse(n: int, p: int) -> int:
  return mod_pow(n, p - 2, p)


@nb.njit
def mod_pow2_inverse(n: int, p: int) -> np.ndarray:
  inv_2 = mod_inverse(2, p)
  a = np.empty(n, np.int64)
  a[0] = 1
  for i in range(n - 1): a[i + 1] = a[i] * inv_2 % p
  return a



@nb.njit
def compress_array(
  a: np.ndarray,
) -> typing.Tuple[(np.ndarray, ) * 2]:
  v = np.unique(a)
  i = np.searchsorted(v, a)
  return i, v


@nb.njit((nb.i8[:], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  n = len(a)
  MOD = 998_244_353
  pow2 = np.ones(1 << 20, np.int64)
  for i in range((1 << 20) - 1):
    pow2[i + 1] = pow2[i] * 2 % MOD
  pow2_inv = mod_pow2_inverse(1 << 20, MOD)
  a, _ = compress_array(a)
  fw = fw_build(fw_op, np.zeros(1 << 20, np.int64))
  cnt = 0
  for i in range(n):
    x = a[i]
    cnt += get_fw(fw, x + 1) * pow2[i - 1] % MOD
    set_fw(fw, x, pow2_inv[i])
  print(cnt % MOD)




def main() -> typing.NoReturn:
  n = int(input())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a)


main()
