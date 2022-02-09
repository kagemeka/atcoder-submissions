def read():
  import sys
  return sys.stdin.buffer.read()


def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_ints():
  *ints, = map(
    int,
    read().split(),
  )
  return ints


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def solve(n, f):
  from collections import (
    defaultdict,
  )
  global mod
  prev = [0] * (n + 1)
  tmp = defaultdict(int)
  for i in range(n):
    prev[i+1] = tmp[f[i]]
    tmp[f[i]] = i + 1

  dp = [0] * (n + 1)
  dp[0] = 1
  l, s = 0, dp[0]
  for i in range(1, n+1):
    while l < prev[i]:
      s -= dp[l]
      s %= mod
      l += 1
    dp[i] = s
    s += dp[i]
    s %= mod
  print(dp[n])


def main():
  n, _ = readline_ints()
  f = read_ints()
  global mod
  mod = 10**9 + 7
  solve(n, f)


if __name__ == '__main__':
  main()
