import sys
from collections import Counter
MOD = 10 ** 9 + 7
n, *a = map(int, sys.stdin.read().split())

def main():
  c = Counter(a)
  ans = 0
  if n & 1:
    for i in range(2, n, 2):
      if c[i] != 2: break
    else:
      if c[0] == 1:
        ans = pow(2, n // 2, MOD)
  else:
    for i in range(1, n, 2):
      if c[i] != 2: break
    else:
      ans = pow(2, n // 2, MOD)
  print(ans)

if __name__ ==  '__main__':
  main()
