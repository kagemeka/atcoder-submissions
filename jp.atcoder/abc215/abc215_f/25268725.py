import typing
import sys
from bisect import (
  bisect_right,
)



def solve(
  xy: typing.List[typing.Tuple[int, int]],
) -> typing.NoReturn:
  n = len(xy)

  xy.sort()
  x, y = zip(*xy)
  mn = [0] * n
  mx = [0] * n
  mn[0] = mx[0] = y[0]
  for i in range(1, n):
    mn[i] = min(mn[i - 1], y[i])
    mx[i] = max(mx[i - 1], y[i])



  def possible(d: int) -> bool:
    for i in range(n):
      j = bisect_right(x, x[i] - d) - 1
      if j < 0: continue
      ok = abs(mn[j] - y[i]) >= d or abs(mx[j] - y[i]) >= d
      if ok: return True
    return False

  def binary_search() -> int:
    lo, hi = 0, 1 << 40
    while hi - lo > 1:
      d = (lo + hi) // 2
      if possible(d):
        lo = d
      else:
        hi = d
    return lo


  print(binary_search())



def main() -> typing.NoReturn:
  n = int(input())
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  *xy, = zip(*[xy] * 2)
  solve(xy)


main()
