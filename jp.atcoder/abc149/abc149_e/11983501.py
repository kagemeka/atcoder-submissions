import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r
from itertools import accumulate

n, m, *a = map(int, sys.stdin.read().split())
a.sort()

def count(border):
  res = 0
  for x in a:
    b = border - x
    res += n - bi_l(a, b)
  return res

def main():
  lo, hi = 1, a[-1] * 2 + 1
  while lo + 1 < hi:
    border = (lo + hi) // 2
    if count(border) >= m:
      lo = border
    else:
      hi = border

  s = a.copy() + [0]
  *s, = accumulate(s[::-1])
  tot = 0
  for x in a:
    b = lo - x
    c = n - bi_l(a, b)
    tot += x * c + s[c]

  tot -= lo * (count(lo) - m)
  print(tot)

if __name__ == '__main__':
  main()
