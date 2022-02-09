import typing
import itertools

def main() -> typing.NoReturn:
    n = int(input())
    a = [1] * n
    for i in range(n - 1):
        a[i] *= 2
    for i in range(1, n):
        a[i] *= 3
    a[0] *= 5
    a[-1] *= 5
    k = 1 << 14
    is_prime = [True] * k
    is_prime[0] = is_prime[1] = False
    for i in range(2, k):
        if i * i > k: break
        if not is_prime[i]: continue
        for j in range(i * i, k, i):
            is_prime[j] = False


    prime_nums = [i for i in range(k) if is_prime[i]]
    cand = []
    for p, q in itertools.combinations(prime_nums, 2):
        if p * q > 10000: continue
        cand.append(p * q)

    for i, x in zip(range(2, n - 1), cand):
        a[i] *= x
    print(*a)

main()
