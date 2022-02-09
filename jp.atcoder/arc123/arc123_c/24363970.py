import sys
import numpy as np


def is_sorted(
  a: np.array,
) -> bool:
  return np.all(
    np.sort(a) == a,
  )


def solve():
  a = np.array(
    list(input()),
    dtype=np.int64,
  )
  a -= 1
  a //= 3
  print(
    4 if not is_sorted(a)
    else a[-1] + 1
  )


def main():
  t = int(input())
  for _ in range(t):
    solve()


main()
