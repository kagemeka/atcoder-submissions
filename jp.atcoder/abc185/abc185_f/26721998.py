import typing
import sys
import numpy as np
import numba as nb


@nb.njit
def bit_length(n: int) -> int:
  l = 1
  while 1 << l <= n: l += 1
  return l


# segment tree normal
S = typing.TypeVar('S')
@nb.njit
def seg_build(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    a: np.ndarray,
) -> np.ndarray:
    r"""Build new segment tree."""
    n = 1 << bit_length(len(a) - 1)
    seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
    for i in range(n << 1): seg[i] = e()
    seg[n:n + len(a)] = a.copy()
    for i in range(n - 1, 0, -1):
        seg[i] = op(seg[i << 1], seg[i << 1 | 1])
    return seg


@nb.njit
def seg_set(
    op: typing.Callable[[S, S], S],
    seg: np.ndarray,
    i: int,
    x: S,
) -> typing.NoReturn:
    r"""Set.

    a_i := x
    """
    i += len(seg) >> 1
    seg[i] = x
    while i > 1:
        i >>= 1
        seg[i] = op(seg[i << 1], seg[i << 1 | 1])


@nb.njit
def seg_get(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    seg: np.ndarray,
    l: int,
    r: int,
) -> int:
    r"""Get.

    return \prod_{j=l}^{r-1}{a_j}
    constraints
        - 0 \le l \le r \le size
    """
    n = len(seg) >> 1
    l, r = l + n, r + n
    vl, vr = e(), e()
    while l < r:
        if l & 1: vl = op(vl, seg[l]); l += 1
        if r & 1: r -= 1; vr = op(seg[r], vr)
        l, r = l >> 1, r >> 1
    return op(vl, vr)


@nb.njit
def seg_max_right(
    op: np.ndarray,
    e: np.ndarray,
    seg: np.ndarray,
    is_ok: typing.Callable[[S, S], bool],
    x: S,
    l: int,
    size: int,
) -> int:
    r"""Max right.

    return maximum index i such that is_ok(\prod_{j=l}^{j=i-1}{a_j}, x).
        here, interface is is_ok(v, x) but is_ok(v)
        so that you should pass x explicitly as an argument,
        because closure is not supported on numba v0.53.1 (on AtCoder).
    """
    n = len(seg) >> 1
    assert 0 <= l < size
    v, i = e(), n + l
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


# segment tree interfaces.
@nb.njit
def build_seg(a: np.ndarray) -> np.ndarray:
    r"""Build interface."""
    return seg_build(seg_op, seg_e, a)

@nb.njit
def set_seg(seg: np.ndarray, i: int, x: S) -> typing.NoReturn:
    r"""Set interface."""
    seg_set(seg_op, seg, i, x)

@nb.njit
def get_seg(seg: np.ndarray, l: int, r: int) -> S:
    r"""Get interface."""
    return seg_get(seg_op, seg_e, seg, l, r)

@nb.njit
def operate_seg(seg: np.ndarray, i: int, x: S) -> typing.NoReturn:
    r"""Operate interface.

    a_i := op(a_i, x)
    """
    set_seg(seg, i, seg_op(get_seg(seg, i, i + 1), x))

@nb.njit
def max_right_seg(
    seg: np.ndarray,
    is_ok: typing.Callable[[S, S], bool],
    x: S,
    l: int,
    size: int,
) -> int:
    r"""Max right interface."""
    return seg_max_right(seg_op, seg_e, seg, is_ok, x, l, size)

@nb.njit
def seg_op(a: S, b: S) -> S: return a ^ b

@nb.njit
def seg_e() -> S: return 0


@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, q = len(a), len(txy)
  seg = build_seg(a)
  for i in range(q):
    t, x, y = txy[i]
    if t == 1:
      operate_seg(seg, x - 1, y)
    else:
      print(get_seg(seg, x - 1, y))


def main() -> typing.NoReturn:
  n, q = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  txy = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(q, 3)

  solve(a, txy)


main()
