import typing


def main() -> None:
    n, m = map(int, input().split())

    # prime factorize m = p0^b0 * p1^b1 * ... pk^bk
    # for each i, answer *= bi // n * pi ( if bi // n = 0, answer *= 1)

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
            answer *= cnt // n * i

    if m > 1 and n == 1:
        answer *= m

    print(answer)

main()
