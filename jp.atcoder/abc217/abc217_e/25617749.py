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

  dq = np.zeros(1 << 20, np.int64)
  dq_l, dq_r = 0, -1

  def deque_append(x):
    nonlocal dq, dq_r
    dq_r += 1
    dq[dq_r] = x

  def deque_appendleft(x):
    nonlocal dq, dq_l
    dq_l -= 1
    dq[dq_l] = x

  def deque_pop():
    nonlocal dq, dq_r
    v = dq[dq_r]
    dq_r -= 1
    return v

  def deque_popleft():
    nonlocal dq, dq_l
    v = dq[dq_l]
    dq_l += 1
    return v

  def deque_empty():
    nonlocal dq_l, dq_r
    return dq_l == dq_r + 1

  while len(a):
    c = a[0]
    if c == 1:
      a = a[1:]
      deque_append(a[0])
    elif c == 2:
      print(heapq.heappop(hq) if hq else deque_popleft())
    elif c == 3:
      while not deque_empty():
        heapq.heappush(hq, deque_popleft())
    a = a[1:]


def main() -> typing.NoReturn:
  q = int(input())
  a = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(a)


main()
