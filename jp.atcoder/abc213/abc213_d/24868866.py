import typing

# dfs

def main():
  n = int(input())
  g = [
    [] for _ in range(n)
  ]
  for _ in range(n - 1):
    a, b = map(
      int, input().split(),
    )
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


  for i in range(n):
    g[i].sort(reverse=1)
  res = []
  parent = [-1] * n
  st = [0]
  visited = [False] * n
  while st:
    u = st.pop()
    res.append(u + 1)
    if visited[u]: continue
    visited[u] = True
    for v in g[u]:
      if v == parent[u]:
        continue
      parent[v] = u
      st.append(u)
      st.append(v)

  print(*res, sep=' ')









main()
