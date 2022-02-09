import typing



def main() -> typing.NoReturn:
    n = int(input())

    cnt = [1] * (n + 1)
    cnt[0] = 0
    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            cnt[j] += 1
    s = 0
    for i in range(1, n + 1):
        s += cnt[i] * i
    print(s)


main()
