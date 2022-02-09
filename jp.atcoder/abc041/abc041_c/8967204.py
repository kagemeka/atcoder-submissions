import sys

n, *a = map(int, sys.stdin.read().split())
a = list(enumerate(a, 1))

def main():
    a.sort(reverse=True, key=lambda x: x[1])
    for i in range(n):
        yield a[i][0]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
