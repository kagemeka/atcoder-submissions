import typing


def solve(
  k: int,
  a: typing.List[int],
) -> typing.NoReturn:
  win = [0] * (1 << 18)
  for i in range(k):
    for x in a:
      win[i + x] |= ~win[i]
  print(
    'First' if win[k]
    else 'Second',
  )


def main() -> typing.NoReturn:
  n, k = map(
    int, input().split(),
  )
  *a, = map(
    int, input().split(),
  )
  solve(k, a)


main()
