import typing
import sys



def solve(
  sd: typing.Iterator[typing.Tuple[str, str]],
  a: int,
  b: int,
) -> typing.NoReturn:
  x = 0
  for s, d in sd:
    d = int(d)
    d = max(a, min(d, b))
    x += d if s == 'East' else  -d
  if x == 0:
    print(0)
  elif x > 0:
    print('East', x)
  else:
    print('West', -x)


def main() -> typing.NoReturn:
  n, a, b = map(int, input().split())
  sd = sys.stdin.read().split()
  sd = zip(*[iter(sd)] * 2)
  solve(sd, a, b)


main()
