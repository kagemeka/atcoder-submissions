import typing

def main() -> typing.NoReturn:
    n, s = input().split()
    n = int(n)

    cnt0 = [0] * (n + 1)
    cnt1 = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'A': cnt0[i + 1] = 1
        elif s[i] == 'T': cnt0[i + 1] = -1
        elif s[i] == 'C': cnt1[i + 1] = 1
        elif s[i] == 'G': cnt1[i + 1] = -1

    for i in range(n):
        cnt0[i + 1] += cnt0[i]
        cnt1[i + 1] += cnt1[i]


    cnt = 0
    for l in range(n - 1):
        for r in range(l + 1, n + 1):
            cnt += cnt0[r] - cnt0[l] == 0 and cnt1[r] - cnt1[l] == 0
    print(cnt)

main()
