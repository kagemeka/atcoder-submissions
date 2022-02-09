import sys
from functools import reduce

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

n, m, *a = map(int, sys.stdin.read().split())

def main():
  for i in range(n):
    a[i] //= 2

  b = set()
  for x in a:
    cnt = 0
    while x % 2 == 0:
      x //= 2
      cnt += 1
    b.add(cnt)
  if len(b) == 2: print(0); return

  l = reduce(lcm, a, 1)
  res = (m // l + 1) // 2
  print(res)

if __name__ == '__main__':
  main()
