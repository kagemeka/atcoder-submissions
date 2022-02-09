import typing
import sys
import numpy as np
import numba as nb
import heapq


@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def solve(
  a: np.ndarray,
) -> typing.NoReturn:
  hq = [0] * 0

  ffq = [0] * 0
  fifo_idx = 0

  def fifo_append(x):
    nonlocal ffq
    ffq.append(x)

  def fifo_pop():
    nonlocal ffq, fifo_idx
    v = ffq[fifo_idx]
    fifo_idx += 1
    return v

  def fifo_empty():
    nonlocal ffq, fifo_idx
    return fifo_idx == len(ffq)

  while len(a):
    c = a[0]
    if c == 1:
      a = a[1:]
      fifo_append(a[0])
    elif c == 2:
      print(heapq.heappop(hq) if hq else fifo_pop())
    elif c == 3:
      while not fifo_empty():
        heapq.heappush(hq, fifo_pop())
    a = a[1:]


def main() -> typing.NoReturn:
  q = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a)


main()
