import typing
import numpy as np
import numba as nb


@nb.njit
def bit_length(n: int) -> int:
    l = 1
    while 1 << l <= n: l += 1
    return l


S = typing.TypeVar('S')
F = typing.TypeVar('F')
@nb.njit
def seg_build(
    op_s: typing.Callable[[S, S], S],
    e_s: typing.Callable[[], S],
    e_f: typing.Callable[[], F],
    a: np.ndarray,
) -> typing.Tuple[np.ndarray, np.ndarray]:
    n = 1 << bit_length(len(a) - 1)
    seg = np.empty((n << 1, ) + a.shape[1:], np.int64)
    for i in range(n << 1): seg[i] = e_s()
    seg[n:n + len(a)] = a.copy()
    for i in range(n - 1, 0, -1):
        seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])
    lazy = np.empty(n, np.int64)
    for i in range(n): lazy[i] = e_f()
    return seg, lazy


@nb.njit
def __seg_apply(
    op_f: typing.Callable[[F, F], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
    f: F,
) -> typing.NoReturn:
    seg[i] = map_(f, seg[i])
    if i < len(lazy): lazy[i] = op_f(f, lazy[i])


@nb.njit
def __seg_propagate(
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
) -> typing.NoReturn:
    __seg_apply(op_f, map_, seg, lazy, i << 1, lazy[i])
    __seg_apply(op_f, map_, seg, lazy, i << 1 | 1, lazy[i])
    lazy[i] = e_f()


@nb.njit
def __seg_merge(
    op_s: typing.Callable[[S, S], S],
    seg: np.ndarray,
    i: int,
) -> typing.NoReturn:
    seg[i] = op_s(seg[i << 1], seg[i << 1 | 1])


@nb.njit
def seg_set(
    op_s: typing.Callable[[S, S], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
    f: F,
) -> typing.NoReturn:
    n = len(seg) >> 1
    assert 0 <= l <= r <= n
    l, r = l + n, r + n
    h = bit_length(n)

    for i in range(h, 0, -1):
        if (l >> i) << i != l:
            __seg_propagate(op_f, e_f, map_, seg, lazy, l >> i)
        if (r >> i) << i != r:
            __seg_propagate(op_f, e_f, map_, seg, lazy, (r - 1) >> i)

    l0, r0 = l, r
    while l < r:
        if l & 1: __seg_apply(op_f, map_, seg, lazy, l, f); l += 1
        if r & 1: r -= 1; __seg_apply(op_f, map_, seg, lazy, r, f)
        l, r = l >> 1, r >> 1
    l, r = l0, r0
    for i in range(1, h + 1):
        if (l >> i) << i != l: __seg_merge(op_s, seg, l >> i)
        if (r >> i) << i != r: __seg_merge(op_s, seg, (r - 1) >> i)


@nb.njit
def seg_get(
    op_s: typing.Callable[[S, S], S],
    e_s: typing.Callable[[], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    l: int,
    r: int,
) -> S:
    n = len(seg) >> 1
    assert 0 <= l <= r <= n
    l, r = l + n, r + n
    h = bit_length(n)

    for i in range(h, 0, -1):
        if (l >> i) << i != l:
            __seg_propagate(op_f, e_f, map_, seg, lazy, l >> i)
        if (r >> i) << i != r:
            __seg_propagate(op_f, e_f, map_, seg, lazy, (r - 1) >> i)

    vl, vr = e_s(), e_s()
    while l < r:
        if l & 1: vl = op_s(vl, seg[l]); l += 1
        if r & 1: r -= 1; vr = op_s(seg[r], vr)
        l, r = l >> 1, r >> 1
    return op_s(vl, vr)


@nb.njit
def seg_update(
    op_s: typing.Callable[[S, S], S],
    op_f: typing.Callable[[F, F], F],
    e_f: typing.Callable[[], F],
    map_: typing.Callable[[F, S], S],
    seg: np.ndarray,
    lazy: np.ndarray,
    i: int,
    x: S,
) -> typing.NoReturn:
    n = len(seg) >> 1
    assert 0 <= i < n
    i += n
    h = bit_length(n)
    for j in range(h, 0, -1):
        __seg_propagate(op_f, e_f, map_, seg, lazy, i >> j)
    seg[i] = x
    for j in range(1, h + 1): __seg_merge(op_s, seg, i >> j)



# lazy segment tree interface.
@nb.njit
def build_seg(a: np.ndarray) -> typing.Tuple[np.ndarray, np.ndarray]:
    return seg_build(seg_op_s, seg_e_s, seg_e_f, a)


@nb.njit
def set_seg(seg: np.ndarray, lazy: np.ndarray, l: int, r: int, f: F) -> typing.NoReturn:
    seg_set(seg_op_s, seg_op_f, seg_e_f, seg_map, seg, lazy, l, r, f)


@nb.njit
def get_seg(seg: np.ndarray, lazy: np.ndarray, l: int, r: int) -> S:
    return seg_get(seg_op_s, seg_e_s, seg_op_f, seg_e_f, seg_map, seg, lazy, l, r)


@nb.njit
def update_point_seg(seg: np.ndarray, lazy: np.ndarray, i: int, x: S) -> typing.NoReturn:
    seg_update(seg_op_s, seg_op_f, seg_e_f, seg_map, seg, lazy, i, x)


MOD = 998_244_353

# set range add, get range mininum.
@nb.njit
def seg_op_s(a: S, b: S) -> S:
    a1, a0 = divmod(a, 1 << 30)
    b1, b0 = divmod(b, 1 << 30)
    c0 = a0 + b0
    c1 = (a1 + b1) % MOD
    return (c1 << 30) + c0

@nb.njit
def seg_e_s() -> S: return 0

@nb.njit
def seg_op_f(f: F, g: F) -> F:
    f1, f0 = divmod(f, 1 << 30)
    g1, g0 = divmod(g, 1 << 30)
    h1 = f1 * g1 % MOD
    h0 = (f1 * g0 + f0) % MOD
    return (h1 << 30) + h0

@nb.njit
def seg_e_f() -> F: return 1 << 30

@nb.njit
def seg_map(f: F, x: S) -> S:
    f1, f0 = divmod(f, 1 << 30)
    x1, x0 = divmod(x, 1 << 30)
    y0 = x0
    y1 = (f1 * x1 + f0 * x0) % MOD
    return (y1 << 30) + y0


import sys


@nb.njit((nb.i8[:], nb.i8[:]), cache=True)
def solve(a: np.ndarray, q: np.ndarray) -> typing.NoReturn:
    seg, lazy = build_seg((a << 30) + 1)
    while q.size:
        if q[0] == 0:
            l, r, b, c = q[1:5]
            q = q[5:]
            set_seg(seg, lazy, l, r, (b << 30) + c)
        else:
            l, r = q[1:3]
            q = q[3:]
            print(get_seg(seg, lazy, l, r) >> 30)



def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    a = np.array(
        sys.stdin.readline().split(),
        dtype=np.int64,
    )
    q = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    )
    solve(a, q)


main()
