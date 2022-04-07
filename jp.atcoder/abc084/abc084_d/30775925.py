def main() -> None:
    q = int(input())
    K = 1 << 17
    is_prime = [True] * K
    is_prime[0] = is_prime[1] = False
    for i in range(2, K):
        if not is_prime[i]:
            continue
        for j in range(i * i, K, i):
            is_prime[j] = False

    is_2017_like = [i & 1 and is_prime[i] and is_prime[(i + 1) // 2] for i in range(K)]

    count = [int(is_2017_like[i]) for i in range(K)]
    for i in range(K - 1):
        count[i + 1] += count[i]

    for _ in range(q):
        l, r = map(int, input().split())
        print(count[r] - count[l - 1])


if __name__ == "__main__":
    main()
