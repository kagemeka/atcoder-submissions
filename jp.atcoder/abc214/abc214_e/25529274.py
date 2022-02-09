import typing
import sys
import numpy as np
import numba as nb


T = typing.TypeVar('T')
@nb.njit
def heappush(
  hq: typing.List[T],
  x: T,
) -> typing.NoReturn:
  i = len(hq)
  hq.append(x)
  while i > 0:
    j = (i - 1) >> 1
    if hq[i] >= hq[j]: break
    hq[i], hq[j] = hq[j], hq[i]
    i = j


T = typing.TypeVar('T')
@nb.njit
def heappop(
  hq: typing.List[T],
) -> T:
  hq[0], hq[-1] = hq[-1], hq[0]
  x = hq.pop()
  i, n = 0, len(hq)
  while 1:
    j = (i << 1) + 1
    if j >= n: break
    j += j < n - 1 and hq[j + 1] < hq[j]
    if hq[i] <= hq[j]: break
    hq[i], hq[j] = hq[j], hq[i]
    i = j
  return x



@nb.njit(
  (nb.i8[:], nb.i8[:]),
  cache=True,
)
def solve(
  l: np.ndarray,
  r: np.ndarray,
) -> typing.NoReturn:
  n = l.size
  idx = np.argsort(l)
  l = l[idx]
  r = r[idx]

  h = [0]
  h.pop()
  i, j = 0, 1
  for _ in range(n):
    if i < n and l[i] == j:
      while i < n and l[i] == j:
        heappush(h, r[i])
        i += 1
    elif not h:
      j = l[i]
      while i < n and l[i] == j:
        heappush(h, r[i])
        i += 1
    if heappop(h) < j:
      print('No')
      return
    j += 1
  print('Yes')


def main() -> typing.NoReturn:
  t = int(input())

  for _ in range(t):
    n = int(input())
    lr = [
      [int(x) for x in sys.stdin.readline().split()]
      for _ in range(n)
    ]
    l, r = np.array(lr).T
    solve(l, r)


main()
