def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def solve(n):
  global mod

  f = [0, 0, 1]
  for _ in range(n-2):
    x = f[-1] + f[-2] + f[-3]
    x %= mod
    f.append(x)
  print(f[n])


def main():
  n = read_int() - 1
  global mod
  mod = 10_007
  solve(n)


if __name__ == '__main__':
  main()
