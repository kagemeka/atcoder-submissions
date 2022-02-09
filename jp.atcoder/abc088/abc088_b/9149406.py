import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    a.sort(reverse=True)
    return sum(a[::2]) - sum(a[1::2])

if __name__ == '__main__':
    ans = main()
    print(ans)
