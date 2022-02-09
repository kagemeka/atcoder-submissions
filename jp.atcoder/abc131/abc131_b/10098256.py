import sys

n, l = map(int, sys.stdin.readline().split())

def main():
    s = (l - 1) * n + (1 + n) * n // 2
    res = []
    for i in range(1, n+1):
        f = l + i - 1
        res.append((abs(f), s - f))

    res.sort()
    return res[0][1]

if __name__=='__main__':
    ans = main()
    print(ans)
