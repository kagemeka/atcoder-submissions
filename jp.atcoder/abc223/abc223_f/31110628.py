import typing


def op(
    left: typing.Tuple[int, int],
    right: typing.Tuple[int, int],
) -> typing.Tuple[int, int]:
    return (left[0] + right[0], min(left[1], left[0] + right[1]))


class SegmentTree:
    __data: typing.List[typing.Tuple[int, int]]
    __size: int

    def __init__(self, size: int) -> None:
        n = 1 << size.bit_length()
        self.__data = [(0, 0)] * (n << 1)
        self.__size = size

    def __len__(self) -> int:
        return self.__size

    def __setitem__(self, i: int, x: typing.Tuple[int, int]) -> None:
        assert 0 <= i < len(self)
        n = len(self.__data) >> 1
        i += n
        self.__data[i] = x
        while i > 1:
            i >>= 1
            self.__data[i] = op(self.__data[i << 1], self.__data[i << 1 | 1])

    def get(self, left: int, right: int) -> typing.Tuple[int, int]:
        assert 0 <= left <= right <= len(self)
        n = len(self.__data) >> 1
        left += n
        right += n
        vl = (0, 0)
        vr = (0, 0)
        while left < right:
            if left & 1:
                vl = op(vl, self.__data[left])
                left += 1
            if right & 1:
                right -= 1
                vr = op(self.__data[right], vr)
            left >>= 1
            right >>= 1
        return op(vl, vr)


def main() -> None:
    # range add range min query
    # 1. lazy segment tree
    # 2. segment tree. each node has (sum for range, min sum from left)
    #   (a, b) + (c, d) = (a + c, min(b, a + d))
    #   e = (0, 0)
    #   default = (0, 0)
    # n, q = map(int, input().split())
    n, q = map(int, input().split())
    s = input()
    a = [1 if c == "(" else -1 for c in s]
    seg = SegmentTree(n)
    for i in range(n):
        seg[i] = (a[i], a[i])
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    for t, l, r in queries:
        l -= 1
        r -= 1
        if t == 1:
            a[l], a[r] = a[r], a[l]
            seg[l] = (a[l], a[l])
            seg[r] = (a[r], a[r])
        else:
            cum, mn = seg.get(l, r + 1)
            print("Yes" if cum == 0 and mn >= 0 else "No")


if __name__ == "__main__":
    main()
