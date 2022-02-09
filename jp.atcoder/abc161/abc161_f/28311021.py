import typing


def find_divisors(n: int) -> typing.List[int]:
    divs = []
    for i in range(1, n + 1):
        if i * i > n: break
        if n % i: continue
        divs.append(i)
        if n // i != i: divs.append(n // i)
    divs.sort()
    return divs


def main() -> typing.NoReturn:
    n = int(input())
    # k is a divisor of N or (N - 1)
    # if N \neq 0 \mod K, the value of N \mod K would not changed.
    # thus, N = 1 \mod K at first. <-> N - 1 = 0 \mod K <-> K|(N - 1), K >= 2
    # if N = 0 \mod K, check wheter K|(N - 1) after dividig N until it become N \leq 0 \mod K

    cnt = len(find_divisors(n - 1)) - 1 # patterns such that N \neq 0 \mod K

    for k in find_divisors(n):
        if k < 2: continue
        m = n
        while m % k == 0: m //= k
        cnt += (m - 1) % k == 0
    print(cnt)

    # O(\sqrt{N} + \sqrt{N}\log{N})

main()
