import typing
import sys
import numpy as np
import numba as nb



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
    for i in range(n << 1):
        seg[i] = e()
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
    n = len(seg) >> 1
    l, r = l + n, r + n
    vl, vr = e(), e()
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
    op: np.ndarray,
    e: np.ndarray,
    seg: np.ndarray,
    is_ok: typing.Callable[[S], bool],
    x: S,
    l: int,
    size: int,
) -> int:
    n = len(seg) >> 1
    assert 0 <= l < size
    v, i = e(), n + l
    while True:
        i //= i & -i
        print(i, -20)
        if is_ok(op(v, seg[i]), x):
            v = op(v, seg[i])
            print(v, -10)
            i += 1
            if i & -i == i:
                return size
            continue
        while i < n:
            i <<= 1
            if not is_ok(op(v, seg[i]), x):
                continue
            v = op(v, seg[i])
            i += 1
        return i - n



@nb.njit
def build_seg(a: np.ndarray) -> np.ndarray:
    return seg_build(seg_op, seg_e, a)


@nb.njit
def set_seg(seg: np.ndarray, i: int, x: S) -> typing.NoReturn:
    seg_set(seg_op, seg, i, x)


@nb.njit
def get_seg(seg: np.ndarray, l: int, r: int) -> S:
    return seg_get(seg_op, seg_e, seg, l, r)


@nb.njit
def operate_seg(
    seg: np.ndarray,
    i: int,
    x: S,
) -> typing.NoReturn:
    set_seg(seg, i, seg_op(get_seg(seg, i, i + 1), x))


@nb.njit
def max_right_seg(
    seg: np.ndarray,
    is_ok: typing.Callable[[S], bool],
    x: S,
    l: int,
    size: int,
) -> int:
    return seg_max_right(seg_op, seg_e, seg, is_ok, x, l, size)


@nb.njit
def seg_op(a: S, b: S) -> S:
    c = a.copy()
    c[1] = min(c[1], c[0] + b[1])
    c[0] += b[0]
    return c


@nb.njit
def seg_e() -> S:
    inf = 1 << 60
    return np.array([0, inf])




@nb.njit((nb.i8[:], nb.i8[:, :]), cache=True)
def solve(a: np.ndarray, q: np.ndarray) -> typing.NoReturn:
    n = len(a)
    s = np.empty((n, 2), np.int64)
    s[:, 0] = a
    s[:, 1] = a

    seg = build_seg(s)
    is_ok = lambda v, x: v >= x

    for i in range(len(q)):
        t, l, r = q[i]
        if t == 0:
            set_seg(seg, l, s[r])
            set_seg(seg, r, s[l])
            tmp = s[r]
            s[r] = s[l]
            s[l] = tmp
            # s[l], s[r] = s[l], s[r]
        else:
            res = get_seg(seg, l, r + 1)
            ans = 'Yes' if res[0] == 0 and res[1] >= 0 else 'No'
            print(ans)

def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    s = [1 if x == '(' else -1 for x in input()]
    s = np.array(s)
    q = np.array(
        sys.stdin.read().split(),
        dtype=np.int64,
    ).reshape(q, 3) - 1
    solve(s, q)


main()
