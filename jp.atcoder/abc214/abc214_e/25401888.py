import typing



def solve(
  l: typing.List[int],
  r: typing.List[int],
) -> typing.NoReturn:
  n = len(l)
  idx = list(range(n))
  idx.sort(key=lambda i: (l[i], r[i]))
  l = [l[i] for i in idx]
  r = [r[i] for i in idx]

  j = -1
  for i in range(n):
    j = max(l[i], j)
    if j <= r[i]:
      j += 1
      continue
    print('No')
    return
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
