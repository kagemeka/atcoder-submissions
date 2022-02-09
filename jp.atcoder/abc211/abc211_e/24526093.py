import typing


def bit_count(
  n: int,
) -> int:
  c = 0
  while n > 0:
    c += n & 1
    n >>= 1
  return c


def solve(
  n: int,
  k: int,
  s: typing.List[str],
) -> typing.NoReturn:
  s = [
    ord(x) - ord('#')
    for x in ''.join(s)
  ]


  def get_nexts(
    i: int,
  ) -> typing.List[int]:
    y, x = divmod(i, n)
    a = []
    if y > 0: a.append(i - n)
    if y < n - 1:
      a.append(i + n)
    if x > 0: a.append(i - 1)
    if x < n - 1:
      a.append(i + 1)
    return a


  searched = set()
  def dfs(
    bits: int,
  ) -> int:
    if bits in searched:
      return 0
    if bit_count(bits) == k:
      return 1
    searched.add(bits)
    tot = 0
    for i in range(n * n):
      if not s[i]: continue
      if ~bits >> i & 1:
        continue
      for j in get_nexts(i):
        if bits >> j & 1:
          continue
        if not s[j]: continue
        nbits = bits | 1 << j
        tot += dfs(nbits)
        searched.add(nbits)
    return tot


  tot = 0
  for i in range(n * n):
    if not s[i]: continue
    tot += dfs(1 << i)
  print(tot)


def main() -> typing.NoReturn:
  n = int(input())
  k = int(input())
  s = [
    input() for _ in range(n)
  ]
  solve(n, k, s)


main()
