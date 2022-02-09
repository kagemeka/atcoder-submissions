import sys

n, *a = map(int, sys.stdin.read().split())

def main():
  s = sum(a)
  if s % 10: ans = s
  else:
    m = min([101] + [x for x in a if x % 10])
    if m == 101: ans = 0
    else: ans = s - m
  print(ans)

if __name__ == '__main__':
  main()
