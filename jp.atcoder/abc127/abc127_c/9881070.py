import sys

n, m, *lr = map(int, sys.stdin.read().split())
lr = zip(*[iter(lr)] * 2)

def main():
    cnt = [0] * (n + 1)
    for l, r in lr:
        cnt[l-1] += 1
        cnt[r] -= 1

    for i in range(n):
        cnt[i+1] += cnt[i]

    res = 0
    for i in range(n):
        res += (cnt[i] == m) & 1

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
