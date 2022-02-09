import sys
from bisect import bisect_right as bi_r, bisect_left as bi_l
inf = float('inf')

n, *a = map(int, sys.stdin.read().split())

def main():
  res = [inf] * n
  for x in a[::-1]:
    res[bi_r(res, x)] = x
  print(bi_l(res, inf))

if __name__ == '__main__':
  main()
