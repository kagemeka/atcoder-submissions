import typing
from heapq import (
  heappush, heappop,
)


def main() -> typing.NoReturn:

  a = []
  n = int(input())

  c = 0
  for _ in range(n):
    q = [
      int(x)
      for x in input().split()
    ]
    if q[0] == 1:
      heappush(a, q[1] - c)
      continue
    if q[0] == 2:
      c += q[1]
      continue
    x = heappop(a)
    print(x + c)





main()
