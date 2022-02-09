import sys
from collections import deque
MOD = 10 ** 9 + 7

n, k, *ab = map(int, sys.stdin.read().split())
graph = [[] for _ in range(n)]
for a, b in zip(*[iter(ab)] * 2):
  a -= 1; b -= 1
  graph[a].append(b)
  graph[b].append(a)

def main():
  for i in range(n):
    if len(graph[i]) + 1 > k:
      print(0)
      return

  cnt = [None] * n; cnt[0] = k
  parent = [None] * n
  stack = [0]
  while stack:
    u = stack.pop()
    c = k - 2 if not parent[u] is None else k - 1
    for v in graph[u]:
      if v == parent[u]: continue
      parent[v] = u
      cnt[v] = c
      c -= 1
      stack.append(v)

  res = 1
  for c in cnt:
    res *= c
    res %= MOD
  print(res)

if __name__ == '__main__':
  main()
