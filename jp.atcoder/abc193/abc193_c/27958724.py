import typing


def main() -> typing.NoReturn:
    m = 1 << 17
    sieve = [True] * m
    n = int(input())
    cnt = n
    for i in range(2, n + 1):
        if i * i > n: break
        if not sieve[i]: continue
        j = i * i
        while j <= n:
            if j < m: sieve[j] = False
            cnt -= 1
            j *= i
    print(cnt)

main()
