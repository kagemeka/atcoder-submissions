import sys
from collections import (
  defaultdict,
)


mod = 10 ** 9 + 7


def main():
  s = input()
  t = '$chokudai'
  ind = dict(
    (c, i)
    for i, c in enumerate(t)
  )
  c = defaultdict(int)
  c['$'] = 1
  for x in s:
    if not x in ind: continue
    c[x] += c[t[ind[x] - 1]]
    c[x] %= mod

  print(c['i'])







main()
