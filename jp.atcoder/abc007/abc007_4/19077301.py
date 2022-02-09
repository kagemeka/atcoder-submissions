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


def f(n: int) -> int:
  ng = set((4, 9))
  *x, = map(int, str(n))
  flg = True
  cnt = 0
  for d in x:
    cnt *= 8
    if not flg: continue
    cnt += d - (d > 4)
    if d in ng: flg = False
  cnt += flg
  return n - cnt


def solve(a: int, b: int) -> None:
  print(f(b) - f(a-1))


def main():
  a, b = readline_ints()
  solve(a, b)


if __name__ == '__main__':
  main()
