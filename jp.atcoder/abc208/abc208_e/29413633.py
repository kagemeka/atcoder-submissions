from __future__ import annotations
import sys
import functools

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, k = map(int, input().split())
    # 0 <= d <= 9
    # except 0,
    # prime factors are only, 2, 3, 5, 7
    # max count is 3 (8 = 2^3)
    # product patterns < (3 * 18 + 1) ^ 4 ~= 10^7
    # cached dfs or defaultdict/map

    sn = str(n)

    @functools.lru_cache(maxsize=None)
    def count_nonzeros(
        i: int,
        no_digit: bool,
        smaller: bool,
        prod: int,
    ) -> int:
        if i == len(sn):
            return not no_digit and prod <= k
        count = 0
        if smaller:
            for d in range(1, 10):
                count += count_nonzeros(i + 1, False, True, prod * d)
            if no_digit:
                assert prod == 1
                count += count_nonzeros(i + 1, True, True, 1)
            else:
                count += count_nonzeros(i + 1, False, True, 0)
        else:
            for d in range(1, int(sn[i])):
                count += count_nonzeros(i + 1, False, True, prod * d)
            if int(sn[i]) == 0:
                count += count_nonzeros(i + 1, False, False, 0)
            else:
                count += count_nonzeros(i + 1, False, False, prod * int(sn[i]))
                if no_digit:
                    assert prod == 1
                    count += count_nonzeros(i + 1, True, True, 1)
                else:
                    count += count_nonzeros(i + 1, False, True, 0)
        return count

    print(count_nonzeros(0, True, False, 1))


if __name__ == "__main__":
    main()
