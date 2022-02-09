def read():
  import sys
  return sys.stdin.buffer.read()


def read_ints():
  *ints, = map(
    int,
    read().split(),
  )
  return ints


def solve(n, d, x, y):
  x, y = abs(x), abs(y)
  if x%d or y%d:
    print(0)
    return

  x, y = x//d, y//d
  r = n - (x + y)
  if r < 0 or r&1:
    print(0)
    return

  from scipy.special import comb
  c = lambda n, r: comb(
    n, r, exact=True,
  )
  res = 0
  half_p = pow(1/2, n)
  for d in range(r//2 + 1):
    south, north = d, y + d,
    west = r//2 - d
    res += half_p * c(n, south) \
      * c(n-south, north) \
      * c(n-south-north, west) \
      * half_p
  print(res)


def main():
  n, d, x, y = read_ints()
  solve(n, d, x, y)


if __name__ == '__main__':
  main()
