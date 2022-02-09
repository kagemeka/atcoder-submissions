import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n - 2):
        k = i + 1
        for j in range(i + 1, n - 1):
            while k + 1 < n and a[k + 1] < a[i] + a[j]: k += 1
            cnt += k - j
    print(cnt)

main()
