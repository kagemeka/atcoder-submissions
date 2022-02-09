import typing
import sys



def solve(
  g: typing.List[
    typing.List[bool],
  ],
) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  h = len(g) - 1
  w = len(g[0]) - 1
  p = [
    [0] * (w + 1)
    for _ in range(h + 1)
  ]
  p[1][1] = 1
  for i in range(h):
    for j in range(w):
      p[i + 1][j + 1] += (
        p[i][j + 1]
        * g[i][j + 1]
        + p[i + 1][j]
        * g[i + 1][j]
      ) % mod
  print(p[-1][-1])


def main() -> typing.NoReturn:
  h, w = map(
    int, input().split(),
  )
  g = [None] * (h + 1)
  g[0] = [False] * (w + 1)
  for i in range(h):
    s = ['#'] + list(input())
    g[i + 1] = [
      x == '.' for x in s
    ]
  solve(g)


main()
