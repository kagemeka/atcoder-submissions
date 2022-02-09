import sys

inf = float('inf')

n, *b = map(int, sys.stdin.read().split())

def main():
    a = [inf] * n
    for i in range(n-1):
        a[i] = min(a[i], b[i])
        a[i+1] = min(a[i+1], b[i])
    return sum(a)

if __name__ == '__main__':
    ans = main()
    print(ans)
