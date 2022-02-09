import typing


def main() -> typing.NoReturn:
    n, m, q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    a = list(map(int, input().split()))
    wv.sort(key=lambda x: (-x[1], x[0]))

    def query(l: int, r: int) -> int:
        b = a[:l] + a[r + 1:]
        b.sort()
        k = len(b)
        used = [False] * k
        s = 0
        for w, v in wv:
            for i, cap in enumerate(b):
                if used[i] or cap < w: continue
                s += v
                used[i] = True
                break
        return s

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        print(query(l, r))


main()
