import typing
import heapq



def solve(
  l: typing.List[int],
  r: typing.List[int],
) -> typing.NoReturn:
  n = len(l)
  idx = list(range(n))
  idx.sort(key=lambda i: (l[i], r[i]))
  l = [l[i] for i in idx]
  r = [r[i] for i in idx]

  h = []
  i, j = 0, 1
  for _ in range(n):
    if i < n and l[i] == j:
      while i < n and l[i] == j:
        heapq.heappush(h, r[i])
        i += 1
    elif not h:
      # if i == n: break
      j = l[i]
      while i < n and l[i] == j:
        heapq.heappush(h, r[i])
        i += 1
    if heapq.heappop(h) < j:
      print('No')
      return
    j += 1
  print('Yes')


def main() -> typing.NoReturn:
  t = int(input())
  for _ in range(t):
    n = int(input())
    l = [-1] * n
    r = [-1] * n
    for i in range(n):
      l[i], r[i] = map(int, input().split())
    solve(l, r)


main()
