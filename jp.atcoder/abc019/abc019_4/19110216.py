def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def inquire(u, v):
  print(f'? {u} {v}', flush=True)
  dist = read_int()
  return dist


def solve(n):
  u = sorted([
    (inquire(1, v), v)
    for v in range(2, n+1)
  ])[-1][1]

  diameter = max(
    inquire(u, v)
    for v in range(1, n+1)
    if u != v
  )
  print(f'! {diameter}')


def main():
  n = read_int()
  solve(n)


if __name__ == '__main__':
  main()
