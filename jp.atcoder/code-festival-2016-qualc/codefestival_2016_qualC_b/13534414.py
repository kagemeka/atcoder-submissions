import sys

def main():
  n, t, *a = map(int, sys.stdin.read().split())
  a.sort()
  b = sum(a) - a[-1]
  a = a[-1]
  ans = max(0, a-(b+1))
  print(ans)

if __name__ == '__main__':
  main()
