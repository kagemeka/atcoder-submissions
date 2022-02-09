import sys

n, *x = map(int, sys.stdin.read().split())

def main():
    m = round(sum(x) / n)
    s = 0
    for i in range(n):
        s += (m - x[i]) ** 2

    return s

if __name__ == '__main__':
    ans = main()
    print(ans)
