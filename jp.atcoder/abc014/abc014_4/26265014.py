import typing
import sys
import numpy as np
import numba as nb

@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while 1 << l <= n: l += 1
  return l


@nb.njit
def euler_tour(
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  n = g[:, :2].max() + 1
  parent = np.full(n, -1, np.int64)
  depth = np.zeros(n, np.int64)
  tour = np.empty(n * 2, np.int64)
  st = [root]
  for i in range(2 * n):
    u = st.pop()
    tour[i] = u
    if u < 0: continue
    st.append(-u - 1)
    for v in g[edge_idx[u]:edge_idx[u + 1], 1][::-1]:
      if v == parent[u]: continue
      parent[v] = u
      depth[v] = depth[u] + 1
      st.append(v)
  return tour, parent, depth


@nb.njit
def bit_length(n: int) -> int:
  l = 0
  while 1 << l <= n: l += 1
  return l


S = typing.TypeVar('S')

@nb.njit
def seg_build(
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  a: np.ndarray,
) -> np.ndarray:
  n = 1 << bit_length(len(a) - 1)
  seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
  for i in range(n << 1): seg[i] = e()
  seg[n:n + len(a)] = a.copy()
  for i in range(n - 1, 0, -1):
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])
  return seg


@nb.njit
def seg_set(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  i: int,
  x: S,
) -> typing.NoReturn:
  i += len(seg) >> 1
  seg[i] = x
  while i > 1:
    i >>= 1
    seg[i] = op(seg[i << 1], seg[i << 1 | 1])


@nb.njit
def seg_get(
  seg: np.ndarray,
  op: typing.Callable[[S, S], S],
  e: typing.Callable[[], S],
  l: int,
  r: int,
) -> int:
  n = len(seg) >> 1
  l, r = l + n, r + n
  vl = vr = e()
  while l < r:
    if l & 1:
      vl = op(vl, seg[l])
      l += 1
    if r & 1:
      r -= 1
      vr = op(seg[r], vr)
    l, r = l >> 1, r >> 1
  return op(vl, vr)


@nb.njit
def seg_max_right(
  seg: np.ndarray,
  op: np.ndarray,
  e: np.ndarray,
  is_ok: typing.Callable[[S], bool],
  x: S,
  l: int,
  size: int,
) -> int:
  n = len(seg) >> 1
  assert 0 <= l < size
  i = l + n
  v = e()
  while True:
    i //= i & -i
    if is_ok(op(v, seg[i]), x):
      v = op(v, seg[i])
      i += 1
      if i & -i == i: return size
      continue
    while i < n:
      i <<= 1
      if not is_ok(op(v, seg[i]), x): continue
      v = op(v, seg[i])
      i += 1
    return i - n



S = typing.TypeVar('S')
@nb.njit
def seg_op(a: S, b: S) -> S:
  return a.copy() if a[0] <= b[0] else b.copy()


@nb.njit
def seg_e() -> S:
  return np.array([1 << 60, -1])


@nb.njit
def build_seg(a: np.ndarray) -> np.ndarray:
  return seg_build(seg_op, seg_e, a)


@nb.njit
def set_point_seg(
  seg: np.ndarray,
  i: int,
  x: S,
) -> typing.NoReturn:
  seg_set(seg, seg_op, i, x)


@nb.njit
def get_range_seg(seg: np.ndarray, l: int, r: int) -> S:
  return seg_get(seg, seg_op, seg_e, l, r)


@nb.njit
def lca_preprocess(
  n: int,
  g: np.ndarray,
  edge_idx: np.ndarray,
  root: int,
) -> np.ndarray:
  tour, parent, depth = euler_tour(g, edge_idx, root)
  for i in range(n * 2):
    if tour[i] < 0: tour[i] = parent[~tour[i]]
  tour = tour[:-1]
  first_idx = np.full(n, -1, np.int64)
  for i in range(n * 2 - 1):
    u = tour[i]
    if first_idx[u] != -1: continue
    first_idx[u] = i
  a = np.empty((len(tour), 2), np.int64)
  a[:, 0], a[:, 1] = depth[tour], tour
  seg = build_seg(a)
  return first_idx, seg



@nb.njit
def lca(
  first_idx: np.ndarray,
  seg: np.ndarray,
  u: int,
  v: int,
) -> int:
  l, r = first_idx[u], first_idx[v]
  if l > r: l, r = r, l
  return get_range_seg(seg, l, r + 1)[1]


@nb.njit
def csgraph_to_directed(g: np.ndarray) -> np.ndarray:
  m = len(g)
  g = np.vstack((g, g))
  g[m:, :2] = g[m:, 1::-1]
  return g


@nb.njit
def sort_csgraph(
  n: int,
  g: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray, np.ndarray]:
  sort_idx = np.argsort(g[:, 0], kind='mergesort')
  g = g[sort_idx]
  edge_idx = np.searchsorted(g[:, 0], np.arange(n + 1))
  original_idx = np.arange(len(g))[sort_idx]
  return g, edge_idx, original_idx


@nb.njit((nb.i8[:, :], nb.i8[:, :]), cache=True)
def solve(xy: np.ndarray, ab: np.ndarray) -> typing.NoReturn:
  n = len(xy) + 1
  g = csgraph_to_directed(xy)
  g, edge_idx, _ = sort_csgraph(n, g)
  first_idx, seg = lca_preprocess(n, g, edge_idx, 0)
  _, _, depth = euler_tour(g, edge_idx, 0)

  def dist(u, v):
    l = lca(first_idx, seg, u, v)
    return depth[u] + depth[v] - 2 * depth[l]

  for i in range(len(ab)):
    a, b = ab[i]
    print(dist(a, b) + 1)



def main() -> typing.NoReturn:
  n = int(input())
  I = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  xy = I[:2 * (n - 1)].reshape(n - 1, 2) - 1
  ab = I[2 * n - 1:].reshape(-1, 2) - 1
  solve(xy, ab)


main()
