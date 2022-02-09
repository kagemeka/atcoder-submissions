import typing
import heapq
import sys




def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = [[] for _ in range(m)]
  for i in range(m):
    k = int(input())
    a[i] = [
      int(x) - 1
      for x in sys.stdin.readline().split()
    ][::-1]

  idx = [[] for _ in range(n)]
  q = []
  for i in range(m):
    j = a[i][-1]
    idx[j].append(i)
    if len(idx[j]) == 2: q.append(j)

  r = n
  for j in q:
    r -= 1
    for i in idx[j]:
      a[i].pop()
      if not a[i]: continue
      k = a[i][-1]
      idx[k].append(i)
      if len(idx[k]) == 2: q.append(k)
  print('Yes' if not r else 'No')







main()
