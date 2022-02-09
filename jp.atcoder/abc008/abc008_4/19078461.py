def read():
  import sys
  return sys.stdin.buffer.read()


def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def read_ints():
  *ints, = map(
    int,
    read().split(),
  )
  return ints


def solve(w: int, h: int) -> None:
  print(count(0, 0, w, h))


from functools import (
  lru_cache,
)
@lru_cache(maxsize=None)
def count(x0, y0, x1, y1) -> int:
  global xy
  res = 0
  for x, y in xy:
    if x < x0 or x >= x1: continue
    if y < y0 or y >= y1: continue
    cnt = x1-x0 + y1-y0 - 1 \
      + count(x0, y0, x, y) \
      + count(x0, y+1, x, y1) \
      + count(x+1, y0, x1, y) \
      + count(x+1, y+1, x1, y1)
    res = max(res, cnt)
  return res


def main():
  w, h = readline_ints()
  _ = read_int()
  global xy
  xy = [x-1 for x in read_ints()]
  *xy, = zip(*[iter(xy)]*2)
  solve(w, h)


if __name__ == '__main__':
  main()
