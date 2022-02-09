import sys
from heapq import (
  heappop,
  heappush,
)




mod = 10 ** 9 + 7



def main():
  n, m = map(
    int,
    input().split(),
  )
  edges = [
    [] for _ in range(n)
  ]
  for _ in range(m):
    a, b = map(
      int,
      input().split(),
    )
    a -= 1; b -= 1
    edges[a].append(b)
    edges[b].append(a)


  inf = float('inf')
  dist = [inf] * n
  dist[0] = 0
  paths = [0] * n
  paths[0] = 1
  q = [(0, 0)]
  while q:
    du, u = heappop(q)
    if dist[u] < du: continue
    for v in edges[u]:
      dv = du + 1
      if dv > dist[v]:
        continue
      elif dv == dist[v]:
        paths[v] += paths[u]
        paths[v] %= mod
        continue

      paths[v] = paths[u]
      dist[v] = dv
      heappush(q, (dv, v))


  print(paths[-1])

main()
