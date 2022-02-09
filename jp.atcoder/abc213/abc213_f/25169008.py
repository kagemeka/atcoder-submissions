import typing
import numpy as np
import sys
import numba as nb


@nb.njit
def sa_doubling(
  a: np.array,
) -> np.array:
  n = a.size
  a = np.searchsorted(
    np.unique(a),
    a,
  )
  cnt = np.zeros(n + 2, dtype=np.int32)

  def count_sort(a):
    for x in a: cnt[x + 1] += 1
    for i in range(n): cnt[i + 1] += cnt[i]
    idx = np.empty(n, dtype=np.int32)
    for i in range(n):
      x = a[i]
      idx[cnt[x]] = i
      cnt[x] += 1
    cnt[:] = 0
    return idx


  k = 1
  rank = a
  while 1:
    b = np.zeros(n, dtype=np.int64)
    for i in range(n - k):
      b[i] = rank[i + k] + 1
    ord_b = count_sort(b)
    a = rank[ord_b]
    ord_a = count_sort(a)
    sa = ord_b[ord_a]
    c = a[ord_a] << 32 | b[sa]
    rank = np.empty(n, np.int64)
    rank[sa[0]] = 0
    for i in range(n - 1):
      rank[sa[i + 1]] = rank[sa[i]] + (c[i + 1] > c[i])
    k *= 2
    if k >= n: break
  return sa



@nb.njit
def kasai(
  a: np.array,
  sa: np.array,
) -> np.array:
  n = a.size
  assert n > 0 and sa.size == n

  rank = np.empty(n, np.int32)
  for i in range(n): rank[sa[i]] = i
  h, l = np.empty(n - 1, np.int64), 0
  for i in range(n):
    if l: l -= 1
    r = rank[i]
    if r == n - 1: continue
    j = sa[r + 1]
    while i + l < n and j + l < n:
      if a[i + l] != a[j + l]: break
      l += 1
    h[r] = l
  return h



@nb.njit(
  (nb.i8[:], ),
  cache=True,
)
def solve(
  a: np.array,
) -> typing.NoReturn:
  n = a.size
  sa = sa_doubling(a)
  lcp = kasai(a, sa)

  a = np.arange(n, 0, -1)
  for _ in range(2):
    st = [(-1, 0)]
    s = 0
    for i in range(n - 1):
      h = lcp[i]
      l = 1
      while st and st[-1][0] >= h:
        x = st.pop()
        l += x[1]
        s -= x[0] * x[1]
      s += h * l
      st.append((h, l))
      a[sa[i + 1]] += s
    sa = sa[::-1]
    lcp = lcp[::-1]

  for x in a: print(x)


def main() -> typing.NoReturn:
  n = int(sys.stdin.buffer.readline().rstrip())
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64)
  solve(s)



main()
