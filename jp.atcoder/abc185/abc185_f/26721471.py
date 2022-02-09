import typing
import sys
import numpy as np
import numba as nb



S = typing.TypeVar('S')
@nb.njit
def fw_build(op: typing.Callable[[S, S], S], a: np.ndarray) -> np.ndarray:
    r"""Build new fenwick tree."""
    n = len(a)
    fw = np.empty((n + 1, ) + a.shape[1:], np.int64)
    fw[1:] = a.copy()
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j < n + 1:
            fw[j] = op(fw[j], fw[i])
    return fw


@nb.njit
def fw_set(
    op: typing.Callable[[S, S], S],
    fw: np.ndarray,
    i: int,
    x: S,
) -> typing.NoReturn:
    r"""Set.

    a_i := op(a_i, x)
    """
    assert 0 <= i < len(fw) - 1
    i += 1
    while i < len(fw):
        fw[i] = op(fw[i], x)
        i += i & -i


@nb.njit
def fw_get(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    fw: np.ndarray,
    i: int,
) -> S:
    r"""Get.

    return \prod_{j=0}^{i-1}{a_i}
    """
    assert 0 <= i < len(fw)
    v = e()
    while i > 0:
        v = op(v, fw[i])
        i -= i & -i
    return v


@nb.njit
def fw_max_right(
    op: typing.Callable[[S, S], S],
    e: typing.Callable[[], S],
    fw: np.ndarray,
    is_ok: typing.Callable[[S, S], bool],
    x: S,
) -> int:
    r"""Max right.

    return maximum index i such that is_ok(\prod_{j=0}^{j=i-1}{a_i}, x).
        here, interface is is_ok(v, x) but is_ok(v)
        so that you should pass x explicitly as an argument,
        because closure is not supported on numba v0.53.1 (on AtCoder).
    """
    n = len(fw)
    l = 1
    while l << 1 < n: l <<= 1
    v, i = e(), 0
    while l:
        if i + l < n and is_ok(op(v, fw[i + l]), x):
            i += l
            v = op(v, fw[i])
        l >>= 1
    return i


# Fenwick Tree interfaces
S = typing.TypeVar('S')
@nb.njit
def build_fw(a: np.ndarray) -> np.ndarray:
    r"""Build interface."""
    return fw_build(fw_op, a)

@nb.njit
def set_fw(fw: np.ndarray, i: int, x: S) -> typing.NoReturn:
    r"""Set interface."""
    fw_set(fw_op, fw, i, x)

@nb.njit
def get_fw(fw: np.ndarray, i: int) -> S:
    r"""Get interface."""
    return fw_get(fw_op, fw_e, fw, i)

@nb.njit
def get_range_fw(fw: np.ndarray, l: int, r: int) -> S:
    r"""Get Range interface.

    target is needed to be Abelian Group but Monoid, that is (S, op, e, inv).
    """
    return fw_op(
        fw_inverse(fw_get(fw_op, fw_e, fw, l)),
        fw_get(fw_op, fw_e, fw, r),
    )

@nb.njit
def max_right_fw(fw: np.ndarray, is_ok: typing.Callable[[S], bool], x: S) -> int:
    r"""Max right interface."""
    return fw_max_right(fw_op, fw_e, fw, is_ok, x)

@nb.njit
def fw_op(a: S, b: S) -> S: return a ^ b

@nb.njit
def fw_e() -> S: return 0

@nb.njit
def fw_inverse(a: S) -> S: return a



@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, txy: np.ndarray) -> typing.NoReturn:
  n, m = len(a), len(txy)
  fw = build_fw(a)
  for j in range(m):
    t, x, y = txy[j]
    if t == 1:
      set_fw(fw, x - 1, y)
    else:
      print(get_range_fw(fw, x - 1, y))


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
