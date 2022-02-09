import typing

def main() -> typing.NoReturn:
    n = int(input())
    k = 1 << 14
    is_prime = [True] * k
    is_prime[0] = is_prime[1] = False
    for i in range(2, k):
        if i * i > k: break
        if not is_prime[i]: continue
        for j in range(i * i, k, i):
            is_prime[j] = False


    cnt = 0
    for i in range(n):
        cnt += is_prime[i]
    print(cnt)


main()
