import typing


def main() -> typing.NoReturn:
    n, s = input().split()
    n = int(n)

    c0 = [0] * n
    c1 = [0] * n
    for i in range(n):
        if s[i] == 'A': c0[i] += 1
        elif s[i] == 'T': c0[i] -= 1
        elif s[i] == 'C': c1[i] += 1
        elif s[i] == 'G': c1[i] -= 1

    for i in range(n - 1):
        c0[i + 1] += c0[i]
        c1[i + 1] += c1[i]
    c0 = [0] + c0
    c1 = [0] + c1


    cnt = 0
    for l in range(n):
        for r in range(l + 1, n + 1):
            cnt += c0[l] == c0[r] and c1[l] == c1[r]
    print(cnt)

main()
