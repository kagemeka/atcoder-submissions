import sys
from collections import Counter

import sys
sys.setrecursionlimit(10**6)
table = dict()
def choose(n, r, mod=None): # not mod, or mod ≠ prime
  if r > n or r < 0: return 0
  if r == 0: return 1
  if (n, r) in table: return table[(n, r)]
  table[(n, r)] = (choose(n - 1, r) + choose(n - 1, r - 1))
  # table[(n, r)] = (choose(n - 1, r, mod) + choose(n - 1, r - 1, mod)) % mod
  return table[(n,r)]

n = int(sys.stdin.readline().rstrip())
s = [''.join(sorted(s)) for s in sys.stdin.read().split()]

def main():
    tot = 0
    for c in Counter(s).values():
        tot += choose(c, 2)
    print(tot)

if __name__ ==  '__main__':
    main()
