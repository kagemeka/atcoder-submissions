

import typing
import numpy as np
import numba as nb


@nb.njit
def extgcd(a: int, b: int) -> typing.Tuple[int, int, int]:
    if b == 0: return a, 1, 0
    g, s, t = extgcd(b, a % b)
    return g, t, s - a // b * t


@nb.njit
def crt(r: np.ndarray, m: np.ndarray) -> typing.Tuple[int, int]:
    r0, m0 = 0, 1
    assert r.size == m.size
    for i in range(r.size):
        r1, m1 = r[i], m[i]
        assert m1 >= 1
        r1 %= m1
        # if m0 < m1:
        #     r0, r1 = r1, r0
        #     m0, m1 = m1, m0
        # if m0 % m1 == 0:
        #     if r0 % m1 != r1: return 0, 0
        #     continue
        g, p, q = extgcd(m0, m1)
        if (r1 - r0) % g: return 0, 0
        u1 = m1 // g
        r0 += (r1 - r0) // g % u1 * p % u1 * m0
        m0 *= u1
        r0 %= m0
    return r0, m0


@nb.njit
def find_divisors(n: int) -> np.ndarray:
    i = np.arange(int(n ** .5) + 1) + 1
    i = i[n % i == 0]
    return np.unique(np.hstack((i, n // i)))


@nb.njit((nb.i8, ), cache=True)
def solve(n: int) -> typing.NoReturn:
    n *= 2
    divs = find_divisors(n)

    mn = 1 << 60
    for a in divs:
        b = n // a
        # g, p, q = extgcd(a, b)
        # if np.gcd(a, b) != 1 or b == 1: continue
        # k = a * (-p % b)
        # mn = min(mn, k)
        rs = np.array([0, -1])
        ms = np.array([a, b])
        r, l = crt(rs, ms)
        if l == 0 or r == 0: continue
        mn = min(mn, r)
    print(mn)



def main() -> typing.NoReturn:
    n = int(input())
    solve(n)

main()
