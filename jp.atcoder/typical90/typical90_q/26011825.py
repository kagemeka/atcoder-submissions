import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, ), cache=True)
def n_choose_2(n: int) -> int:
  return n * (n - 1) // 2 if n >= 2 else 0


@nb.njit
def fw_build(n: int) -> np.ndarray:
  return np.zeros(n + 1, np.int64)


@nb.njit
def fw_set(fw: np.ndarray, i: int, x: int) -> typing.NoReturn:
  while i < len(fw):
    fw[i] += x
    i += i & -i


@nb.njit
def fw_get(fw: np.ndarray, i: int) -> int:
  v = 0
  while i > 0:
    v += fw[i]
    i -= i & -i
  return v


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(n: int, lr: np.ndarray) -> typing.NoReturn:
  m = len(lr)

  lr = lr[np.argsort(lr[:, 1], kind='mergesort')]
  lr = lr[np.argsort(lr[:, 0], kind='mergesort')]

  def count_complements():
    def same_end():
      b = np.bincount(lr.ravel())
      cnt = 0
      for x in b:
        cnt += n_choose_2(x)
      return cnt

    def exclusive():
      cnt = 0
      dp = np.zeros(n + 1, np.int64)
      j = 0
      for i in range(m):
        l, r = lr[i]
        dp[r] += 1
        while j < l - 1:
          dp[j + 1] += dp[j]
          j += 1
        cnt += dp[l - 1]
      return cnt

    def inclusive():
      fw = fw_build(n)
      cnt = 0
      for i in range(m):
        l, r = lr[i]
        cnt += i - fw_get(fw, r)
        fw_set(fw, r, 1)
      return cnt

    return same_end() + exclusive() + inclusive()

  print(n_choose_2(m) - count_complements())



def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  lr = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2)
  solve(n, lr)


main()
