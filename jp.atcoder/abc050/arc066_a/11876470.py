import sys
from collections import Counter
MOD = 10 ** 9 + 7
n, *a = map(int, sys.stdin.read().split())

def main():
  c = Counter(a)
  if n & 1:
    if c[0] != 1:
      print(0); return
  for i in range(1 + (n & 1), n, 2):
    if c[i] != 2:
      print(0); return
  print(pow(2, n // 2, MOD))

if __name__ ==  '__main__':
  main()
