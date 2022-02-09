import sys
import numpy as np
from heapq import heappush, heappop
from bisect import bisect_left as bi_l, bisect_right as bi_r
from collections import deque, Counter, defaultdict
from itertools import product
inf = float('inf')
MOD = 10**9+7
# MOD = 998244353


class ABC001():
  def A():
    h1, h2 = map(int, sys.stdin.read().split())
    print(h1-h2)

  def B(): pass
  def C(): pass
  def D(): pass


class ABC002():
  def A():
    x, y = map(int, sys.stdin.readline().split())
    print(max(x, y))

  def B():
    vowels = set('aeiou')
    s = sys.stdin.readline().rstrip()
    t = ''
    for c in s:
      if c in vowels: continue
      t += c
    print(t)

  def C():
    *coords, = map(int, sys.stdin.readline().split())
    def triangle_area(x0, y0, x1, y1, x2, y2):
      x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0;
      return abs(x1*y2 - x2*y1) / 2
    print(triangle_area(*coords))

  def D(): pass



if __name__ == '__main__':
  ABC002.C()
