import sys
import numpy as np
MOD = 10 ** 9 + 7

n = int(sys.stdin.readline().rstrip())
a = np.array(sys.stdin.readline().split(), dtype=np.int64)

def main():
  x = a[:, None] >> np.arange(61) & 1
  x = x.sum(axis=0)
  y = n - x
  res = x * y  % MOD * ((1 << np.arange(61)) % MOD)
  print(res.sum() % MOD)

if __name__ == '__main__':
  main()
