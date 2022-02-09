import typing
import numpy as np


def solve(
  g: np.array,
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  h, w = g.shape
  p = np.zeros(
    w,
    np.int64,
  )
  p[0] = 1
  for i in range(h):
    np.cumsum(p, out=p)
    p -= np.maximum.accumulate(
      p * ~g[i],
    )
    p *= g[i]
    p %= mod
  print(p[-1])


def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  g = [
    [
      x == '.'
      for x in list(input())
    ]
    for _ in range(h)
  ]
  g = np.array(g)
  solve(g)


main()
