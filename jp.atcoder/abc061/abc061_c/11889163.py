import sys

n, k, *ab = map(int, sys.stdin.read().split())

def main():
  cnt = 0
  for a, b in sorted(zip(*[iter(ab)] * 2)):
    cnt += b
    if cnt >= k:
      print(a)
      return

if __name__ == '__main__':
  main()
