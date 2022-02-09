import typing



def compress(a: typing.List[int]) -> typing.Tuple[(typing.List[int], ) * 2]:
    import bisect
    v = sorted(set(a))
    return [bisect.bisect_left(v, x) for x in a], v



class Fenwick():
    def __init__(self, a: typing.List[int]) -> typing.NoReturn:
        n = len(a)
        d = [0] * (n + 1)
        d[1:] = a.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n: continue
            d[j] += d[i]
        self.__data = d


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




def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    # \sum_{i=0}^{n-2}\sum_{j=i+1, a_j >= a_i}^{n-1}2^{j-i-1}
    # = \sum_{i=0}^{n-2}\sum_{j=i+1, a_j >= a_i}^{n-1}2^{j-1} * 2^{-i}
    # = \sum_{j=1}^{n-1}\sum_{i=0, a_i <= a_j}^{j-1}2^{j-1} * 2^{-i}
    # = \sum_{j=1}^{n-1}2^{j-1}\sum_{i=0, a_i <= a_j}^{j-1}2^{-i}
    # \sum_{i=0, a_i <= a_j}^{j-1}2^{-i} can be calculated O(\log{N}) with array compression and fenwick tree.


    a, retrieve = compress(a)

    fw = Fenwick([0] * len(retrieve))

    # pow_2 = [0] * n
    # pow_2_inv = [0] * n
    # pow_2[0] = pow_2_inv[0] = 1
    pow_2 = pow_2_inv = 1
    MOD = 998_244_353
    inv = pow(2, -1, MOD)
    s = 0
    for i in range(n):
        s += pow_2 * inv % MOD * fw[a[i] + 1] % MOD
        s %= MOD
        fw[a[i]] = pow_2_inv
        pow_2 = pow_2 * 2 % MOD
        pow_2_inv = pow_2_inv * inv % MOD
    print(s)


main()
