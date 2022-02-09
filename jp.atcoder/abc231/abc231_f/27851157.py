import typing



def compress_array(a: typing.List[int]) -> typing.Tuple[(typing.List[int], ) * 2]:
    r"""Compress array.

    return
        compressed_array
        retrieve_array
    """
    import bisect
    v = sorted(set(a))
    return [bisect.bisect_left(v, x) for x in a], v


import typing



class FenwickTree():
    def __init__(self, a: typing.List[int]) -> typing.NoReturn:
        n = len(a)
        fw = [None] * (n + 1)
        fw[1:] = a.copy()
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j < n + 1: fw[j] = fw[j] + fw[i]
        self.__data = fw

    def __setitem__(self, i: int, x: int) -> typing.NoReturn:
        d = self.__data
        assert 0 <= i < len(d) - 1
        i += 1
        while i < len(d):
            d[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        d = self.__data
        assert 0 <= i < len(d)
        v = 0
        while i > 0:
            v += d[i]
            i -= i & -i
        return v

    # def max_right(self, is_ok: typing.Callable[[S], bool]) -> int:
    #     m, d = self.__m, self.__data
    #     n = len(d)
    #     l = 1
    #     while l << 1 < n: l <<= 1
    #     v, i = m.e(), 0
    #     while l:
    #         if i + l < n and is_ok(m.op(v, d[i + l])):
    #             i += l
    #             v = m.op(v, d[i])
    #         l >>= 1
    #     return i



def count_inversion(a: typing.List[int]) -> int:
    a, _ = compress_array(a)
    n = len(a)
    fw = FenwickTree([0] * n)
    c = 0
    for i in range(n):
        x = a[i]
        c += i - fw[x]
        fw[x] = 1
    return c



import collections

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = list(zip(a, b))
    ab.sort(key=lambda x: (x[0], -x[1]))
    b = [x[1] for x in ab]
    # sort_idx = sorted(range(n), key=lambda i: a[i])
    # b = [b[i] for i in sort_idx]
    cnt = count_inversion(b)


    tmp = collections.defaultdict(int)
    for x in ab:
        tmp[x] += 1
    for x in tmp.values():

        cnt += x * (x - 1) // 2

    print(cnt + n)

main()
