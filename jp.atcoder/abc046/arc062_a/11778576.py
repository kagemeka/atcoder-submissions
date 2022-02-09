import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
res = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, 2)

def main():
  for i in range(n - 1):
    res[i+1] *= ((res[i] + res[i+1] - 1) // res[i+1]).max()
  print(res[n-1].sum())

if __name__ ==  '__main__':
  main()
