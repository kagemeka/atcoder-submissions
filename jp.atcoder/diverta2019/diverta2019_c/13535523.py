import sys

def main():
  n, *S = sys.stdin.read().split()
  a = b = ba = 0
  cnt = 0
  for s in S:
    cnt += s.count('AB')
    bl2 = s[0] == 'B'
    bl1 = s[-1] == 'A'
    a += bl1
    b += bl2
    ba += bl1 & bl2

  if a == b:
    cnt += a - (a == ba)
  else:
    cnt += min(a, b)

  print(cnt)

if __name__ == '__main__':
  main()
