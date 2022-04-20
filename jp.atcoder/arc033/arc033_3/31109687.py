import typing


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.__data = [0] * (size + 1)

    def __len__(self) -> int:
        return len(self.__data) - 1

    def __setitem__(self, i: int, x: int) -> None:
        assert 0 <= i < len(self)
        i += 1
        while i <= len(self):
            self.__data[i] += x
            i += i & -i

    def __getitem__(self, i: int) -> int:
        assert 0 <= i <= len(self)
        v = 0
        while i > 0:
            v += self.__data[i]
            i -= i & -i
        return v

    def binary_search_right(self, is_ok: typing.Callable[[int], bool]) -> int:

        v = 0
        i = 0
        n = len(self.__data)
        length = 1 << (n.bit_length() - 1)
        while length:
            if i + length < n and is_ok(v + self.__data[i + length]):
                i += length
                v += self.__data[i]
            length >>= 1
        return i


def main() -> None:
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    fw = FenwickTree(1 << 18)
    for t, x in queries:
        if t == 1:
            fw[x] = 1
        else:
            i = fw.binary_search_right(lambda y: y < x)
            print(i)
            fw[i] = -1


if __name__ == "__main__":
    main()
