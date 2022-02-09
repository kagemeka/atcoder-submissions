import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    border = (k ** 2 + 1) // 2

    def possible(med: int) -> bool:
        s = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                s[i + 1][j + 1] = 1 if a[i][j] <= med else 0
        for i in range(n):
            for j in range(1, n + 1):
                s[i + 1][j] += s[i][j]
        for j in range(n):
            for i in range(1, n + 1):
                s[i][j + 1] += s[i][j]

        for i in range(k, n + 1):
            for j in range(k, n + 1):
                cnt = s[i][j] - s[i - k][j] - s[i][j - k] + s[i - k][j - k]
                if cnt >= border: return True
        return False

    def binary_search() -> int:
        lo, hi = -1, 1 << 30
        while hi - lo > 1:
            med = (lo + hi) >> 1
            if possible(med):
                hi = med
            else:
                lo = med
        return hi
    print(binary_search())

main()
