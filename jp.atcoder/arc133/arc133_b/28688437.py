import typing
import bisect


class FenwickTree:  # version not using dataclass for performance.
    def __init__(self, arr: typing.List[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] = max(data[j], data[i])
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self.__data) - 1
        i += 1
        while i < len(self.__data):
            self.__data[i] = max(self.__data[i], x)
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self.__data)
        v = 0
        while i > 0:
            v = max(v, self.__data[i])
            i -= i & -i
        return v


def main() -> None:
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    divisor_indices = [[] for _ in range(n + 1)]
    for i, x in enumerate(p):
        for y in range(x, n + 1, x):
            divisor_indices[y].append(i + 1)
    # index = [0] * (n + 1)
    # dp = [[(0, -1)] * 2 for _ in range(n + 1)]
    # # (count, last index)
    # for i, x in enumerate(q):
    #     # y = q[i]


    # print(divisor_indices)
    fw = FenwickTree([0] * (n + 1))
    # dp = [0] * (n + 1)
    for x in q:
        for last in divisor_indices[x][::-1]:
            # dp[last] = max(dp[last], dp[last - 1] + 1)
            fw[last] = fw[last] + 1
    #     print(dp)
    # print(dp)
    print(fw[n + 1])



if __name__ == "__main__":
    main()
