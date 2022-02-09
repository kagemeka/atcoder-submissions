import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = list(map(int, input().split()))
    a.sort()
    f.sort(reverse=True)



    def possible(x: int) -> bool:
        cost = 0
        for i in range(n):
            cost += max(0, a[i] - x // f[i])
        return cost <= k


    def binary_search() -> int:
        # is it possible to make all product a_i * f_i <= x
        lo, hi = -1, 1 << 50 # impossible, possible
        while hi - lo > 1:
            x = (lo + hi) // 2
            if possible(x): hi = x
            else: lo = x
        return hi

    x = binary_search()
    print(x)

main()
