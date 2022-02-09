import typing

def main() -> typing.NoReturn:
    n = int(input())
    k = 55_555
    is_prime = [True] * (k + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, k + 1):
        if i * i > k: break
        if not is_prime[i]: continue
        for j in range(i * i, k + 1, i):
            is_prime[j] = False

    cand = [i for i in range(k + 1) if is_prime[i] and i % 5 == 2]
    print(*cand[:n])

main()
