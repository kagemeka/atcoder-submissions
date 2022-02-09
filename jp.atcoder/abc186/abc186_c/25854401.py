import typing
import numpy as np
import numba as nb



@nb.njit((nb.i8[:], nb.i8), cache=True)
def base10_from_nary(bits: np.ndarray, base: int) -> int:
  assert abs(base) >= 2
  n = 0
  d = 1
  for b in bits:
    n += d * b
    d *= base
  return n


@nb.njit((nb.i8, nb.i8), cache=True)
def base10_to_nary(n: int, base: int) -> np.ndarray:
  assert abs(base) >= 2
  bits = np.empty(64, np.int64)
  i = 0
  while True:
    n, r = divmod(n, base)
    if r < 0:
      n += 1
      r -= base
    bits[i] = r
    i += 1
    if n == 0: break
  return bits[:i]



@nb.njit((nb.i8, ), cache=True)
def solve(
  n: int,
) -> typing.NoReturn:
  def contain_7(n):
    bits = base10_to_nary(n, 8)
    for b in bits:
      if b == 7:
        return True
    while n:
      n, r = divmod(n, 10)
      if r == 7:
        return True
    return False


  cnt = 0
  for i in range(1, n + 1):
    cnt += not contain_7(i)
  print(cnt)



def main() -> typing.NoReturn:
  n = int(input())
  solve(n)


main()
