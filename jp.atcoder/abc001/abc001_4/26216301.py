import typing
import sys
import numpy as np



def transform(time: int) -> int:
  return time // 100 * 60 + time % 100


def transform_inverse(time: int) -> int:
  return time // 60 * 100 + time % 60


def main() -> typing.NoReturn:
  n = int(input())
  se = list(map(
    lambda x: tuple(map(int, x.split('-'))),
    sys.stdin.read().split(),
  ))

  s, e = np.array(se).T
  s = s // 5 * 5
  e = (e + 4) // 5 * 5
  s = transform(s)
  e = transform(e)

  m = 1440
  a = np.zeros(m + 2, np.int64)
  np.add.at(a, s, 1)
  np.subtract.at(a, e + 1, 1)
  a = a.cumsum().tolist()


  se = []
  raining = False
  start = -1
  for i in range(m + 2):
    if a[i] == 0:
      if not raining: continue
      se.append((start, i - 1))
      raining = False
    else:
      if raining: continue
      start = i
      raining = True

  for s, e in se:
    s = transform_inverse(s)
    e = transform_inverse(e)
    print(f'{s:04}-{e:04}')


main()
