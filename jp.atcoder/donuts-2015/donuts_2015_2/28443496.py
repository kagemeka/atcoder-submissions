import typing



def popcount(n: int) -> int:
    """Popcount.

    Args:
        n (int): an 64-bit signed or unsigned integer.

    Returns:
        int: popcount := count of active binary bits.

    Complexity:
        time: O(1)
        space: O(1)

    Examples:
        >>> popcount(0b1010)
        2
        >>> popcount(0b1100100)
        3
        >>> popcount(-1)
        64
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007F


def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    b = [-1] * m
    t = [0] * m
    for i in range(m):
        b[i], _, *c = map(int, input().split())
        for j in c:
            t[i] |= 1 << (j - 1)


    mx = 0
    for s in range(1 << n):
        tot = 0
        cnt = 0
        for i in range(n):
            if ~s >> i & 1: continue
            cnt += 1
            tot += a[i]
        if cnt != 9: continue
        for i in range(m):
            tot += b[i] * (popcount(t[i] & s) >= 3)
        mx = max(mx, tot)
    print(mx)

main()
