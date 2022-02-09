import typing
import sys
import numpy as np
import numba as nb



def rps(a: str, b: str) -> int:
  if a == b: return 0
  if a == 'G' and b == 'C': return 1
  if a == 'C' and b == 'P': return 1
  if a == 'P' and b == 'G': return 1
  if a == 'C' and b == 'G': return -1
  if a == 'P' and b == 'C': return -1
  if a == 'G' and b == 'P': return -1


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  a = sys.stdin.read().split()

  score = [0] * (n << 1)
  # rank = list(range(n << 1))

  for i in range(m):
    order = sorted(range(n << 1), key=lambda x: (-score[x], x))
    for j in range(n):
      j *= 2
      b, c = order[j], order[j + 1]
      res = rps(a[b][i], a[c][i])
      if res == 0: continue
      if res == 1:
        score[b] += 1
      else:
        score[c] += 1


  order = sorted(range(n << 1), key=lambda x: -score[x])
  for x in order:
    print(x + 1)

main()
