import typing


class FenwickTree():
    def __init__(self, a: typing.List[int]) -> typing.NoReturn:
        n = len(a)
        data = [0] * (n + 1)
        data[1:] = a.copy()
        for i in range(1, n):
            j = i + (i & -i)
            if j > n: continue
            data[j] += data[i]
        self.__data = data


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
    h, w, m = map(int, input().split())
    yx = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    min_y = [h] * w
    min_x = [w] * h
    for y, x in yx:
        min_y[x] = min(min_y[x], y)
        min_x[y] = min(min_x[y], x)

    cnt = 0
    for x in range(min_x[0], w):
        min_y[x] = 0
    for y in range(min_y[0], h):
        min_x[y] = 0

    cnt = sum(min_y)
    a = [1] * w
    fw = FenwickTree(a)
    indices = [[] for _ in range(h + 1)]
    for x in range(w):
        indices[min_y[x]].append(x)

    for y in range(h):
        for x in indices[y]:
            fw[x] = -1

        cnt += min_x[y] - fw[min_x[y]]
    print(cnt)



main()
