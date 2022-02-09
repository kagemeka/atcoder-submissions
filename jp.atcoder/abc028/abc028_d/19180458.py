def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def solve(n, k):
  c = (3 * 2 * (n - k) * (k - 1) \
    + 3 * (n - 1) \
    + 1
  ) / (n ** 3)
  print(c)


def main():
  n, k = readline_ints()
  solve(n, k)


if __name__ == '__main__':
  main()
