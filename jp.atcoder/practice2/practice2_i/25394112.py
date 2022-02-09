import typing
import sys
import numpy as np
import numba as nb





@nb.njit((nb.i8[:], ))
def sa_is(
  a: np.array,
) -> np.array:
  if a.min() <= 0: a += 1
  assert (a > 0).all()
  a = np.hstack((a, np.array([0])))
  n, m = a.size, a.max() + 1

  is_s = np.ones(n, dtype=np.bool8)
  for i in range(n - 1, 0, -1):
    is_s[i - 1] = (
      is_s[i] if a[i - 1] == a[i] else
      a[i - 1] < a[i]
    )
  is_lms = np.zeros(n, dtype=np.bool8)
  # is_lms[np.arange(1, n)[~is_s[:-1] & is_s[1:]]] = True
  for i in range(1, n):
    is_lms[i] = is_s[i] & ~is_s[i - 1]

  lms = np.flatnonzero(is_lms)

  b = np.zeros(m, dtype=np.int64)
  for x in a: b[x] += 1

  def _induce():
    sa = np.full(n, -1, dtype=np.int64)
    sa_idx = b.cumsum()
    for i in lms[::-1]:
      x = a[i]
      sa_idx[x] -= 1
      sa[sa_idx[x]] = i

    sa_idx = b.copy()
    s = 0
    for i in range(m):
      s, sa_idx[i] = s + sa_idx[i], s
    for i in range(n):
      i = sa[i] - 1
      if i < 0 or is_s[i]: continue
      x = a[i]
      sa[sa_idx[x]] = i
      sa_idx[x] += 1

    sa_idx = b.cumsum()
    for i in range(n - 1, -1, -1):
      i = sa[i] - 1
      if i < 0 or not is_s[i]: continue
      x = a[i]
      sa_idx[x] -= 1
      sa[sa_idx[x]] = i

    return sa


  sa = _induce()


  def _correct_lms_order():
    nonlocal lms
    lms_idx = sa[is_lms[sa]]
    l = lms_idx.size
    na = np.full(n, -1, dtype=np.int64)
    na[-1] = i = 1
    for j in range(l - 1):
      j, k = lms_idx[j], lms_idx[j + 1]
      for d in range(n):
        j_is_lms = is_lms[j + d]
        k_is_lms = is_lms[k + d]
        if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms:
          i += 1; break
        if d > 0 and j_is_lms | k_is_lms: break
      na[k] = i
    na = na[na > 0]
    if i == l:
      lms_order = np.full(l, -1, dtype=np.int64)
      for i in range(l):
        lms_order[na[i] - 1] = i
    else:
      lms_order = sa_is(na)
    lms = lms[lms_order]


  _correct_lms_order()
  sa = _induce()
  return sa[1:]



@nb.njit
def lcp_kasai(
  a: np.array,
  sa: np.array,
) -> np.array:
  n = a.size
  assert n > 0 and sa.size == n

  rank = np.argsort(sa)
  h, l = np.empty(n - 1, np.int32), 0
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
  a: np.ndarray,
) -> typing.NoReturn:
  sa = sa_is(a)
  lcp = lcp_kasai(a, sa)
  n = a.size
  s = n * (n + 1) // 2
  print(s - lcp.sum())



def main() -> typing.NoReturn:
  s = np.frombuffer(
    sys.stdin.buffer.readline().rstrip(),
    dtype='b',
  ).astype(np.int64) - ord('a') + 1
  solve(s)


main()
