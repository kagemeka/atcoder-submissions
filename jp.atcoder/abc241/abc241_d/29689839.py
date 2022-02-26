# import heapq
import typing


class FenwickTreeIntAdd:
    def __init__(self, arr: typing.List[int]) -> None:
        n = len(arr)
        data = [0] * (n + 1)
        data[1:] = arr.copy()
        for i in range(n):
            j = i + (i & -i)
            if j > n:
                continue
            data[j] += data[i]
        self.__data = data

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i < len(self) + 1:
            self.__data[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i <= len(self)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v

    def get_range(self, left: int, right: int) -> int:

        return self[right] - self[left]

    def max_right(self, is_ok: typing.Callable[[int], bool]) -> int:
        n = len(self) + 1
        length = 1
        while length << 1 < n:
            length <<= 1
        v, i = 0, 0
        while length:
            if i + length < n and is_ok(v + self.__data[i + length]):
                i += length
                v += self.__data[i]
            length >>= 1
        return i


class FenwickTreeMultiset:
    __max_value: int

    def __init__(self, max_value: int) -> None:
        """instance can contain values range of [0, max_value)."""
        self.__fw = FenwickTreeIntAdd([0] * max_value)
        self.__max_value = max_value

    @property
    def max_value(self) -> int:
        return self.__max_value

    def __len__(self) -> int:
        return self.__fw[self.max_value]

    def __contains__(self, x: int) -> bool:
        return self.count(x) >= 1

    def count(self, x: int) -> int:
        if x < 0 or self.max_value <= x:
            return 0
        return self.__fw.get_range(x, x + 1)

    def is_empty(self) -> bool:
        return len(self) == 0

    def __bool__(self) -> bool:
        return not self.is_empty()

    def insert(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = 1

    def remove(self, x: int) -> None:
        if x not in self:
            raise KeyError(x)
        self.__fw[x] = -1

    def remove_all(self, x: int) -> None:
        assert 0 <= x < self.max_value
        self.__fw[x] = -self.count(x)

    def __getitem__(self, i: int) -> typing.Optional[int]:
        """Return i-th element."""
        if not 0 <= i < len(self):
            return None
        return self.__fw.max_right(lambda v: v < i + 1)

    def min(self) -> typing.Optional[int]:
        return None if len(self) == 0 else self[0]

    def max(self) -> typing.Optional[int]:
        return None if len(self) == 0 else self[len(self) - 1]

    def lower_bound(self, x: int) -> int:
        return self.__fw[x]

    def upper_bound(self, x: int) -> int:
        return self.__fw[x + 1]


import bisect


def compress(arr: typing.List[int]) -> typing.Tuple[typing.List[int], typing.List[int]]:
    import bisect

    v = sorted(set(arr))
    return (
        [bisect.bisect_left(v, x) for x in arr],
        v,
    )


def main() -> None:
    min_q = []
    max_q = []
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    cand = []
    for query in queries:
        x = query[1]
        # if query[0] == 1:
        cand.append(x)
        # if len(query) == 2:
        #     x = query[1]
        #     min_q.append(x)
        #     min_q.sort()
        #     min_q = min_q[:5]
        #     max_q.append(x)
        #     max_q.sort()
        #     max_q = max_q[-5:]
    _, values = compress(cand)

    ms = FenwickTreeMultiset(len(values))
    for query in queries:
        x = query[1]
        v = bisect.bisect_left(values, x)
        if len(query) == 2:
            ms.insert(v)
            continue
            # min_q.append(x)
            # min_q.sort()
            # min_q = min_q[:5]
            # max_q.append(x)
            # max_q.sort()
            # max_q = max_q[-5:]

        k = query[2]
        if query[0] == 2:
            i = ms.upper_bound(v)
            print(-1 if i < k else values[ms[i - k]])
        else:
            i = ms.lower_bound(v)
            # print(i, x, v)
            print(-1 if i + k - 1 >= len(ms) else values[ms[i + k - 1]])


if __name__ == "__main__":
    main()
