import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8, nb.i8[:, :]), cache=True)
def solve(w_max: int, vw: np.ndarray) -> typing.NoReturn:
  n = len(vw)

  def enumerate_all(vw):
    n = len(vw)
    a = np.empty((1 << n, 2), np.int64)
    for s in range(1 << n):
      v = w = 0
      for i in range(n):
        if ~s >> i & 1: continue
        v += vw[i, 0]
        w += vw[i, 1]
      a[s] = (v, w)
    mx = -1
    a = a[np.argsort(a[:, 1], kind='mergesort')]
    for i in range((1 << n) - 1):
      a[i + 1, 0] = max(a[i + 1, 0], a[i, 0])
    return a

  if n <= 30:
    a, b = vw[:n // 2], vw[n // 2:]
    a = enumerate_all(a)
    b = enumerate_all(b)
    v_max = 0
    for i in range(len(a)):
      av, aw = a[i]
      if aw > w_max: break
      j = np.searchsorted(b[:, 1], w_max - aw, side='right')
      v_max = max(v_max, av + b[j - 1, 0])
    print(v_max)

  elif np.all(vw[:, 0] <= 1000):
    inf = 1 << 60
    s = vw[:, 0].sum()
    dp = np.full(s + 1, inf, np.int64)
    dp[0] = 0
    for i in range(n):
      v, w = vw[i]
      for j in range(s, v - 1, -1):
        dp[j] = min(dp[j], dp[j - v] + w)
    for i in range(s, -1, -1):
      if dp[i] <= w_max: return i

  elif np.all(vw[:, 1] <= 1000):
    s = vw[:, 1].sum()
    if w_max > s:
      print(vw[:, 0].sum())
      return
    dp = np.zeros(s + 1, np.int64)
    for i in range(n):
      v, w = vw[i]
      for j in range(s, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
    print(dp[w_max])


def main() -> typing.NoReturn:
  n, w = map(int, input().split())
  vw = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(n, 2)
  solve(w, vw)


main()
