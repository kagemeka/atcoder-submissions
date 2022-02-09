import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    cnt = [0, 0, 0]
    q, r = divmod(m, 4)

    # 3 + 3 == 2 + 4 なので、老人は偶奇合わせだけで良い。
    if r == 3:
        cnt[1] += 1
        n -= 1
    elif r == 1:
        cnt[0] += 1
        cnt[1] += 1
        q -= 1
        n -= 2
    elif r == 2:
        cnt[0] += 1
        n -= 1

    # r == 0の状態

    possible = True
    if q < 0:
        possible = False
    elif n < q or q * 2 < n:
        possible = False

    if not possible:
        print(-1, -1, -1)
        sys.exit()

    cnt[0] += (n - q) * 2
    cnt[2] += q * 2 - n
    print(*cnt, sep=' ')

if __name__ == '__main__':
    main()
