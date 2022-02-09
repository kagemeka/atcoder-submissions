def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def solve(n):
  cnt = 0
  for i in range(9):
    pp = pow(10, i + 1)
    p = pow(10, i)
    cc = n // pp * p
    c = n % pp - p + 1
    c = min(max(c, 0), p)
    cnt += cc + c

  print(cnt)


def main():
  n = read_int()
  solve(n)


if __name__ == '__main__':
  main()
