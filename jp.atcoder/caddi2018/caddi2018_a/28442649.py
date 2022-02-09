import typing


def main() -> None:
    n, m = map(int, input().split())

    # prime factorize m = p0^b0 * p1^b1 * ... pk^bk
    # for each i, answer *= p1 ^ (bi // n)

    answer = 1

    for i in range(2, m + 1):
        if i * i > m:
            break
        if m % i:
            continue
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        if cnt // n >= 1:
            answer *= pow(i, cnt // n)

    answer *= pow(m, 1 // n)

    print(answer)

main()
