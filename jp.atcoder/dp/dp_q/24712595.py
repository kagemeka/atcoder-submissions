import typing



def get_mx(
  bit: typing.List[int],
  i: int,
) -> int:
  mx = -(1 << 50)
  while i > 0:
    mx = max(mx, bit[i])
    i -= i & -i
  return mx


def set_val(
  bit: typing.List[int],
  i: int,
  x: int,
) -> typing.NoReturn:
  while i < len(bit):
    bit[i] = max(bit[i], x)
    i += i & -i


def solve(
  n: int,
  h: typing.List[int],
  a: typing.List[int],
) -> typing.NoReturn:
  indices = sorted(
    range(n),
    key=lambda i: h[i],
  )
  inf = 1 << 50
  bit = [-inf] * (n + 1)
  for i in indices:
    v = get_mx(bit, i + 1)
    a[i] = max(a[i], a[i] + v)
    set_val(bit, i + 1, a[i])
  print(max(a))




def main() -> typing.NoReturn:
  n = int(input())
  *h, = map(
    int, input().split(),
  )
  *a, = map(
    int, input().split(),
  )
  solve(n, h, a)


main()
