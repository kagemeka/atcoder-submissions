import typing
import sys



def solve(
  n: int,
  xy: typing.Generator,
) -> typing.NoReturn:
  indeg = [0] * n
  edges = [
    [] for _ in range(n)
  ]
  for x, y in xy:
    x -= 1; y -= 1
    edges[x].append(y)
    indeg[y] += 1

  q = [
    v for v in range(n)
    if not indeg[v]
  ]
  dist = [0] * n
  for u in q:
    for v in edges[u]:
      dv = dist[u] + 1
      if dv <= dist[v]:
        continue
      dist[v] = dv
      q.append(v)

  print(max(dist))



def main() -> typing.NoReturn:
  n, m = map(
    int, input().split(),
  )
  xy = map(
    int,
    sys.stdin.read().split(),
  )
  xy = zip(*[xy] * 2)
  solve(n, xy)


main()
