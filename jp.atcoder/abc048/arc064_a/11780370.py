import sys

n, x, *a = map(int, sys.stdin.read().split())
a = [0] + a

def main():
  tot = 0
  for i in range(1, n + 1):
    if a[i] + a[i-1] > x:
      tot += a[i] + a[i-1] - x
      a[i] = x - a[i-1]
  print(tot)

if __name__ ==  '__main__':
  main()
