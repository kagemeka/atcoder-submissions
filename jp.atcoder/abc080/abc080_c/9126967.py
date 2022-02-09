import sys

*I, = map(int, sys.stdin.read().split())
n = I[0]
f = list(zip(*[iter(I[1:1+10*n])] * 10))
p = list(zip(*[iter(I[1+10*n:])] * 11))

def main():
    res = -float('inf')
    for i in range(1, 2**10):
        cnt = [0] * n
        for j in range(10):
            if i >> j & 1:
                for k in range(n):
                    cnt[k] += f[k][j]
        profit = 0
        for k in range(n):
            profit += p[k][cnt[k]]
        res = max(res, profit)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
