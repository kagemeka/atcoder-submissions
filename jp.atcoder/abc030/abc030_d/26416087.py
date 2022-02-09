import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8, nb.i8[:]), cache=True)
def solve(
  b: np.ndarray,
  a: int,
  k: np.ndarray,
) -> typing.NoReturn:
  n = len(b)
  start = a
  order = np.full(n, -1, np.int64)
  for i in range(n + 1):
    if order[a] != -1:
      loop_start = order[a]
      loop = i - loop_start
      break
    order[a] = i
    a = b[a]

  def k_is_small():
    v = 0
    for x in k[::-1]:
      v = v * 10 + x
      if v > loop_start: return False
    return True

  if k_is_small():
    i = start
    v = 0
    for x in k[::-1]:
      v = v * 10 + x
    for _ in range(v):
      i = b[i]
    print(i + 1)
    return

  v = 0
  for x in k[::-1]:
    v = v * 10 + x
    v %= loop
  v -= loop_start
  v %= loop
  for _ in range(v):
    a = b[a]
  print(a + 1)


def main() -> typing.NoReturn:
  n, a = map(int, sys.stdin.buffer.readline().split())
  k = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='S1',
  ).astype(np.int64)[::-1]
  b = np.array(
    sys.stdin.buffer.readline().split(),
    dtype=np.int64,
  ) - 1
  a -= 1
  solve(b, a, k)


main()
