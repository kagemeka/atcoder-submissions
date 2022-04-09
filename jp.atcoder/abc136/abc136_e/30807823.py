import typing


def find_divisors(n: int) -> typing.List[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    divisors.sort()
    return divisors


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # all elements in a after the operations are multiple of x.
    # thus, the sum of the array must be multiple of x.
    # the sum is not gonna be changed through each operation.

    # the kinds of candidate of x is up to O(\sqrt{N * max(A)}).
    # <= about 2,500

    # fix x and check whether the value is able to be achieved or not.

    # sort the array in order of negative diff (or positive) to x.

    mx = 1  # clearly.
    tot = sum(a)

    def possible(divisor: int) -> bool:
        b = [x % divisor for x in a]
        b.sort()
        s = sum(b)
        # right_count * divisor - (s - sum_to_subtract_left) = sum_to_add_right
        # sum_to_subtract_left = sub_to_add_right

        to_subtract = 0
        for i in range(n):
            to_subtract += b[i]
            to_add = (n - i - 1) * divisor - (s - to_subtract)
            if to_add != to_subtract:
                continue
            break  # this condition must be satisfied at least once.
        else:
            raise
        return to_subtract <= k

    for d in find_divisors(tot)[1:]:
        if not possible(d):
            continue
        mx = max(mx, d)
    print(mx)


if __name__ == "__main__":
    main()
