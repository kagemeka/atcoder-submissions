import typing
import collections


class PrimeFactorize():
  def __call__(
    self,
    n: int,
  ) -> typing.DefaultDict[int, int]:
    f = collections.defaultdict(int)
    i = 2
    while i * i <= n:
      while n % i == 0:
        n //= i
        f[i] += 1
      i += 1
    if n > 1: f[n] = 1
    return f


def solve(
  a: typing.List[int],
  m: int,
) -> typing.NoReturn:
  n = len(a)
  fn = PrimeFactorize()

  p = [False] * (1 << 20)
  for x in a:
    for i in fn(x): p[i] = True

  s = [True] * (m + 1)
  s[0] = False
  for i in range(m + 1):
    if not p[i] or not s[i]: continue
    for j in range(i, m + 1, i):
      s[j] = False

  print(sum(s))
  for i in range(m + 1):
    if s[i]: print(i)


def main() -> typing.NoReturn:
  n, m = map(int, input().split())
  *a, = map(int, input().split())
  solve(a, m)


main()
