import typing


def find_divisors(n: int) -> typing.List[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if n // i != i:
            divisors.append(n // i)
    divisors.sort()
    return divisors


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    K = 1 << 18
    count = [0] * K
    for x in a:
        count[x] += 1

    tot = 0
    for i in range(K):
        if count[i] == 0:
            continue
        for j in find_divisors(i):
            tot += count[i] * count[j] * count[i // j]
        # print(i, tot)
    print(tot)


if __name__ == "__main__":
    main()
