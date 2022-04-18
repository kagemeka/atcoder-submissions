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


class FenwickTree:
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


class ArrayCompression:
    """

    Examples:
    >>> a = [3, 10, 2, 5]
    >>> compress = ArrayCompression(a)
    >>> compressed = [compress(x) for x in a]
    >>> compressed
    [1, 3, 0, 2]
    >>> equal_to_original = [compress.retrieve(x) for x in compressed]
    >>> equal_to_original
    [3, 10, 2, 5]
    """

    __values: typing.List[int]

    def __init__(self, array: typing.List[int]) -> None:
        self.__values = sorted(set(array))

    def __call__(self, value: int) -> int:
        import bisect

        i = bisect.bisect_left(self.__values, value)
        if i >= len(self.__values) or self.__values[i] != value:
            raise KeyError
        return i

    def retrieve(self, key: int) -> int:
        return self.__values[key]


def main() -> None:
    n = int(input())
    s = list(map(int, input().split()))
    compress = ArrayCompression(s)
    s = [compress(x) for x in s]
    ms = FenwickTree(len(s))
    s.sort()
    for x in s[:-1]:
        ms.insert(x)

    a = [s[-1]]
    for _ in range(n):
        b = []
        for x in a:
            i = ms.lower_bound(x)
            if i == 0:
                print("No")
                return
            v = ms[i - 1]
            b.append(v)
            ms.remove(v)
        a += b
    print("Yes")


if __name__ == "__main__":
    main()
