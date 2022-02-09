import typing
import sys
import numpy as np
import numba as nb




@nb.njit
def _induce(
  a: np.ndarray,
  is_s: np.ndarray,
  lms: np.ndarray,
  bucket: np.ndarray,
) -> np.ndarray:
  n, m = a.size, bucket.size
  sa = np.full(n, -1, np.int64)

  def _set_lms():
    sa_idx = bucket.cumsum()
    for i in lms[::-1]:
      x = a[i]
      sa_idx[x] -= 1
      sa[sa_idx[x]] = i

  def _induce_l():
    sa_idx = bucket.copy()
    s = 0
    for i in range(m):
      s, sa_idx[i] = s + sa_idx[i], s
    for i in range(n):
      i = sa[i] - 1
      if i < 0 or is_s[i]: continue
      x = a[i]
      sa[sa_idx[x]] = i
      sa_idx[x] += 1

  def _induce_s():
    sa_idx = bucket.cumsum()
    for i in range(n - 1, -1, -1):
      i = sa[i] - 1
      if i < 0 or not is_s[i]: continue
      x = a[i]
      sa_idx[x] -= 1
      sa[sa_idx[x]] = i

  _set_lms()
  _induce_l()
  _induce_s()
  return sa


@nb.njit
def _preprocess(a, m):
  n = a.size
  is_s = np.ones(n, np.bool8)
  for i in range(n - 1, 0, -1):
    is_s[i - 1] = (
      is_s[i] if a[i - 1] == a[i] else
      a[i - 1] < a[i]
    )
  is_lms = np.zeros(n, np.bool8)
  is_lms[np.arange(1, n)[~is_s[:-1] & is_s[1:]]] = True
  lms = np.flatnonzero(is_lms)

  bucket = np.zeros(m, np.int32)
  for x in a: bucket[x] += 1

  return (is_s, is_lms, lms, bucket)


@nb.njit
def _compute_next_array(
  a: np.ndarray,
  sa: np.ndarray,
  is_lms: np.ndarray,
) -> np.ndarray:
  n = a.size
  lms_idx = sa[is_lms[sa]]
  l = lms_idx.size
  na = np.full(n, -1, dtype=np.int64)
  na[-1] = i = 0
  for j in range(l - 1):
    j, k = lms_idx[j], lms_idx[j + 1]
    for d in range(n):
      j_is_lms = is_lms[j + d]
      k_is_lms = is_lms[k + d]
      if a[j + d] != a[k + d] or j_is_lms ^ k_is_lms:
        i += 1; break
      if d > 0 and j_is_lms | k_is_lms: break
    na[k] = i
  na = na[na >= 0]
  return na


@nb.njit
def sa_is(
  a: np.ndarray,
) -> np.ndarray:
  if a.min() <= 0: a += 1
  assert (a > 0).all()
  a = np.hstack((a, np.array([0])))
  m = a.max() + 1

  st = []
  while True:
    n = a.size
    is_s, is_lms, lms, b = _preprocess(a, m)
    sa = _induce(a, is_s, lms, b)
    st.append((a, is_s, lms, b))

    a = _compute_next_array(a, sa, is_lms)
    l = lms.size
    if a.max() < l - 1: continue
    lms_order = np.argsort(a)
    break

  while st:
    a, is_s, lms, b = st.pop()
    lms = lms[lms_order]
    lms_order = _induce(a, is_s, lms, b)

  return lms_order[1:]



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
