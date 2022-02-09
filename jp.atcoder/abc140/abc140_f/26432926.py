import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8, nb.i8[:], ), cache=True)
def solve(n: int, s: np.ndarray) -> typing.NoReturn:
  s = np.sort(s)[::-1]
  cnt = np.zeros(1 << n, np.int64)
  cnt[0] = n
  ptr = 1
  for i in range(1 << n):
    for j in range(cnt[i]):
      if s[ptr] >= s[i]:
        print('No')
        return
      cnt[ptr] = cnt[i] - j - 1
      ptr += 1
  print('Yes')


def main() -> typing.NoReturn:
  n = int(input())
  s = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(n, s)


main()
