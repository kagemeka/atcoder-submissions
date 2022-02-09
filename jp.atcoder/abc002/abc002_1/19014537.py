def readline():
  import sys
  return \
    sys.stdin.buffer.readline()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def solve(x: int, y: int):
  print(max(x, y))


def main():
  x, y = readline_ints()
  solve(x, y)


if __name__ == '__main__':
  main()
