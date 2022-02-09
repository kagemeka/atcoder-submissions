import sys

n, *a = map(int, sys.stdin.read().split())

def main():
  x = round(sum(a) / n)
  s = 0
  for i in range(n):
    s += pow(x - a[i], 2)
  print(s)

if __name__ == '__main__':
  main()
