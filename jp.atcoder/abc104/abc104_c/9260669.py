import sys

n, G = map(int, sys.stdin.readline().split())
G //= 100
p = []
t = []
for i in range(1, n+1):
    pi, ci = map(int, sys.stdin.readline().split())
    p.append(pi)
    t.append(i * pi + ci // 100)

def main():
    res = sum(p)
    for i in range(2 ** n - 1):
        s = 0
        cnt = 0
        for j in range(n):
            if i >> j & 1:
                s += t[j]
                cnt += p[j]
            else:
                m = j + 1
        if s < G:
            tmp = (G - s + m - 1) // m
            if tmp < p[m-1]:
                cnt += tmp
            else:
                continue
        res = min(res, cnt)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
