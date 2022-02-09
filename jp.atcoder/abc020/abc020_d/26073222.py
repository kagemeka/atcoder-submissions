import typing


class FindDivisors():
  def __call__(self, n: int) -> typing.List[int]:
    divs = []
    i = 1
    while i * i < n:
      if n % i:
        i += 1
        continue
      divs.append(i)
      divs.append(n // i)
      i += 1
    if i * i == n: divs.append(i)
    return sorted(divs)


class PrimeFactors():
  def __call__(self, n: int) -> typing.List[int]:
    factors = []
    i = 2
    while i * i <= n:
      if n % i:
        i += 1
        continue
      factors.append(i)
      while n % i == 0: n //= i
    if n > 1: factors.append(n)
    return factors



def solve(n: int, k: int) -> typing.NoReturn:
  mod = 10 ** 9 + 7
  divs = FindDivisors()(k)

  m = len(divs)
  s = [0] * m
  for i in range(m):
    d = divs[i]
    s[i] = (d + n // d * d) * (n // d) // 2 % mod

  for i in range(m - 1, -1, -1):
    for j in range(i + 1, m):
      if divs[j] % divs[i]: continue
      s[i] -= s[j]
    s[i] %= mod

  cnt = 0
  for i in range(m):
    cnt += k // divs[i] * s[i] % mod
  print(cnt % mod)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  solve(n, k)


main()
