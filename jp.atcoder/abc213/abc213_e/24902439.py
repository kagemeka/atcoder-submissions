import typing
from collections import (
  deque,
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

  q = deque()
  q.append((0, 0))


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


  while q:
    i, j = q.popleft()
    for di, dj in dij:
      ni = i + di
      nj = j + dj
      if not on_grid(ni, nj):
        continue
      if s[i][j] == '#':
        continue
      d = dist[i][j]
      if d >= dist[ni][nj]:
        continue
      dist[ni][nj] = d
      q.appendleft((ni, nj))

    for di in range(-2, 3):
      for dj in range(-2, 3):
        md = abs(di) + abs(dj)
        if md == 4 or md == 0:
          continue
        ni = i + di
        nj = j + dj
        if not on_grid(ni, nj):
          continue
        d = dist[i][j] + 1
        if d >= dist[ni][nj]:
          continue
        dist[ni][nj] = d
        q.append((ni, nj))


  print(dist[-1][-1])





main()
