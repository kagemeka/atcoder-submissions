import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    b = sorted(a.copy())
    m1 = b[-1]
    m2 = b[-2]
    if m1 == m2:
        res = [m1] * n
    else:
        res = [None] * n
        for i in range(n):
            if a[i] < m1:
                res[i] = m1
            else:
                res[i] = m2
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
