import sys

n, x, *a = map(int, sys.stdin.read().split())

def main():
  cnt = 0
  lim = x
  for c in a:
    if c > lim:
      cnt += c - lim
      lim = x - lim
    else:
      lim = x - c
  print(cnt)

if __name__ ==  '__main__':
  main()
