import sys

n, m, *x = map(int, sys.stdin.read().split())

def main():
    x.sort()
    s = x[-1] - x[0]
    d = [0] + sorted([x[i+1] - x[i] for i in range(m-1)], reverse=True)
    for i in range(m-1):
        d[i+1] += d[i]

    return s - d[min(n, m)-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
