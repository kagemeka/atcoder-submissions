import typing
import sys
import numpy as np
# import numba as nb
import functools

# @nb.njit
def bit_count(n: int) -> int:
  cnt = 0
  while n:
    cnt += n & 1
    n >>= 1
  return cnt


# @nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(b: np.ndarray, c: np.ndarray) -> typing.NoReturn:
  total_score = b.sum() + c.sum()
  b, c = b.tolist(), c.tolist()


  def calc_chokudai_score(board: int) -> typing.NoReturn:
    s = 0
    for y in range(2):
      for x in range(3):
        i = y * 3 + x
        j = i + 3
        s += b[y][x] * (board >> i & 1 == board >> j & 1)
    for y in range(3):
      for x in range(2):
        i = y * 3 + x
        j = i + 1
        s += c[y][x] * (board >> i & 1 == board >> j & 1)
    return s

  n = 9

  @functools.lru_cache(maxsize=None)
  def dfs(board: int, used: int) -> int:
    used_cnt = bit_count(used)
    if used_cnt == n:
      return calc_chokudai_score(board)

    turn = (9 - used_cnt) & 1
    cand = []
    for i in range(n):
      if used >> i & 1: continue
      cand.append(dfs(board | turn << i, used | 1 << i))
    return max(cand) if turn == 1 else min(cand)

  x = dfs(0, 0)
  y = total_score - x
  print(x, y)


def main() -> typing.NoReturn:
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  b = I[:6].reshape(2, 3)
  c = I[6:].reshape(3, 2)
  solve(b, c)


main()
