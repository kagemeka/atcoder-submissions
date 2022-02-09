import typing
from heapq import (
  heappush,
  heappop,
)


def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  s = [
    input()
    for _ in range(h)
  ]

  inf = 1 << 20
  dist = [
    [inf] * w
    for _ in range(h)
  ]
  dist[0][0] = 0


  dij = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
  )
  def on_grid(
    i: int,
    j: int,
  ) -> bool:
    return (
      0 <= i < h and
      0 <= j < w
    )

  q = [(0, 0, 0)]

  while q:
    d, i, j = heappop(q)
    if d > dist[i][j]:
      continue
    for di, dj in dij:
      ni = i + di
      nj = j + dj
      if not on_grid(ni, nj):
        continue
      if s[i][j] == '#':
        continue
      if d >= dist[ni][nj]:
        continue
      dist[ni][nj] = d
      heappush(q, (d, ni, nj))

    for di in range(-2, 3):
      for dj in range(-2, 3):
        md = abs(di) + abs(dj)
        if md == 4 or md == 0:
          continue
        ni = i + di
        nj = j + dj
        if not on_grid(ni, nj):
          continue
        nd = d + 1
        if nd >= dist[ni][nj]:
          continue
        dist[ni][nj] = nd
        heappush(
          q,
          (nd, ni, nj),
        )


  print(dist[-1][-1])


main()
