import typing




def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input()))
    x = input()

    dp = [0] * (n + 1)
    dp[-1] = 1 << 0
    b = [0] * 7
    for i in range(7):
        b[i * 10 % 7] = i

    for i in range(n - 1, -1, -1):
        d = a[i] % 7
        if x[i] == 'A':
            cnt = [0] * 7
            for j in range(7):
                if ~dp[i + 1] >> j & 1: continue
                cnt[b[(j - d) % 7]] += 1
                cnt[b[j]] += 1
            for j in range(7):
                if cnt[j] == 2:
                    dp[i] |= 1 << j
            if dp[i] == 0:
                print('Aoki')
                return
        else:
            for j in range(7):
                if ~dp[i + 1] >> j & 1: continue
                dp[i] |= 1 << b[(j - d) % 7]
                dp[i] |= 1 << b[j]
    print('Takahashi')

main()
