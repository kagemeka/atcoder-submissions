import sys
import functools


@functools.lru_cache
def f(n):
  if n == 0: return 0
  for k in range(1, 6):
    for r in range(
      k, 3 * k + 1,
    ):
      q = n - r
      if q % 10: continue
      if f(q // 10) <= k:
        return k


def main():
  for x in map(
    int,
    open(0).read().split()[1:],
  ):
    print(f(x))


main()
