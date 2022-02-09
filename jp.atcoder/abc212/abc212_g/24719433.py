import typing


def find_divisors(
  n: int,
) -> typing.List[int]:
  a = []
  i = 1
  while i * i < n:
    if n % i: i += 1; continue
    a.append(i)
    a.append(n // i)
    i += 1
  if i * i == n: a.append(i)
  a.sort()
  return a


def main() -> typing.NoReturn:
  mod = 998244353
  p = int(input())
  n = p - 1

  divs = find_divisors(n)[::-1]
  l = len(divs)
  cnt = [0] * l
  for i in range(l):
    d = divs[i]
    c = n // d
    for j in range(i):
      if divs[j] % d: continue
      c -= cnt[j]
    cnt[i] = c % mod

  s = 1
  for i in range(l):
    s += n // divs[i] * cnt[i]
    s %= mod
  print(s)


main()
