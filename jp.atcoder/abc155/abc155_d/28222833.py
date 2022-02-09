import typing
import bisect

def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    neg = []
    pos = []
    zero_cnt = 0
    for x in a:
        if x == 0: zero_cnt += 1
        elif x < 0: neg.append(x)
        elif x > 0: pos.append(x)


    inf = 1 << 60
    s = len(neg) * len(pos)
    if s >= k:
        # answer is negative.

        def possible(x: int) -> bool:
            cnt = 0
            # cnt >= k -> ok
            i = 0
            for y in pos:
                # y * z <= x
                # z <= x // y
                while i < len(neg) and neg[i] <= x // y: i += 1
                cnt += i
            return cnt >= k


        def binary_search() -> int:
            lo, hi = -inf, -1 # ng, ok

            while hi - lo > 1:
                x = (lo + hi) // 2
                if possible(x): hi = x
                else: lo = x
            return hi

        print(binary_search())
        return

    s += zero_cnt * (len(neg) + len(pos)) + zero_cnt * (zero_cnt - 1) // 2
    if s >= k:
        # answer is 0
        print(0)
        return

    # answer is positive
    k -= s

    neg.reverse()
    neg = [-x for x in neg]

    def count(a: typing.List[int], x: int) -> int:
        n = len(a)
        cnt = 0
        i = -1
        for j in range(1, n):
            if i == j - 2: i += 1
            y = a[j]
            # y * z <= x
            while i >= 0 and a[i] > x // y: i -= 1
            cnt += i + 1
        return cnt

    def possible(x: int) -> bool:
        return count(pos, x) + count(neg, x) >= k


    def binary_search():
        lo, hi = 0, inf # ng, ok
        while hi - lo > 1:
            x = (lo + hi) // 2
            if possible(x): hi = x
            else: lo = x
        return hi
    print(binary_search())



main()
