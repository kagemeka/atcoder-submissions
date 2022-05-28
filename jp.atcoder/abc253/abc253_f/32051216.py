import typing


class FenwickTreeIntAdd:
    def __init__(self, arr: list[int]) -> None:
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


class DualFenwickTreeIntAdd:
    def __init__(self, arr: list[int]) -> None:
        n = len(arr)
        assert n > 0
        delta = [arr[0]]
        for i in range(n - 1):
            delta.append(arr[i + 1] - arr[i])
        self.__fw = FenwickTreeIntAdd(delta)

    def set(self, left: int, right: int, x: int) -> None:
        n = len(self.__fw)
        assert 0 <= left < right <= n
        self.__fw[left] = x
        if right < n:
            self.__fw[right] = -x

    def __getitem__(self, i: int) -> int:
        assert 0 <= i < len(self.__fw)
        return self.__fw[i + 1]


def main() -> None:
    n, m, q = map(int, input().split())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    update_query_index = [None] * q
    latest_update_index = [None] * n
    # print(queries)
    for i in range(q):
        query = queries[i]
        t = query[0]
        if t == 1:
            continue
        if t == 2:
            j = query[1] - 1
            latest_update_index[j] = i
        else:
            j = query[1] - 1
            # print(i, j)
            update_query_index[i] = latest_update_index[j]

    # print(update_query_index)
    for_what_columns = [[] for _ in range(q)]
    for i in range(q):
        j = update_query_index[i]
        if j is None:
            continue
        col = queries[i][2] - 1
        for_what_columns[j].append(col)
    # print(for_what_columns)
    for i in range(q):
        for_what_columns[i] = for_what_columns[i][::-1]  # queue to statck
    # print(for_what_columns)
    # print(update_query_index)

    fw = DualFenwickTreeIntAdd([0] * m)
    row_deltas = [[] for _ in range(n)]
    # print(queries)
    for i in range(q):
        query = queries[i]
        t = query[0]
        if t == 1:
            l, r, x = query[1], query[2], query[3]
            l -= 1
            r -= 1
            fw.set(l, r + 1, x)
        elif t == 2:
            j, x = query[1], query[2]
            j -= 1
            assert not row_deltas[j]
            # print(for_what_columns[i])
            for col in for_what_columns[i]:
                row_deltas[j].append(x - fw[col])
        else:
            j, k = query[1], query[2]
            j -= 1
            k -= 1
            v = fw[k]
            if update_query_index[i] is None:
                print(v)
            else:
                assert row_deltas[j]
                v += row_deltas[j].pop()
                print(v)

        # print(row_deltas, i)


if __name__ == "__main__":
    main()
