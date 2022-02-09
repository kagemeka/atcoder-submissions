import sys

n, m = map(int, sys.stdin.readline().split())
g = [[int(x) for x in sys.stdin.readline().split()[1:]] for _ in range(n)]

def main():
    res = set(range(1, m+1))
    for a in g:
        res &= set(a)

    return len(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
