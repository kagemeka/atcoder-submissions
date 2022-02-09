import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = [1 if x == 'R' else 2 if x == 'G' else 3 for x in input()]


    s = [[0] * (n + 1) for _ in range(4)]
    for i in range(n, 0, -1):
        for j in range(4):
            s[j][i - 1] = s[j][i]
        x = a[i - 1]
        s[x][i - 1] += 1

    cnt = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if a[i] == a[j]: continue
            x = a[i] ^ a[j]
            cnt += s[x][j + 1]
            k = 2 * j - i
            if k <= n - 1 and a[k] == x:
                cnt -= 1
    print(cnt)

main()
