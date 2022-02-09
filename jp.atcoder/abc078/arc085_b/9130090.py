import sys

n, z, w, *a = map(int, sys.stdin.read().split())

def main():
    if n == 1:
        return abs(a[n-1] - w)
    return max(abs(a[n-1] - w), abs(a[n-1] - a[n-2]))

if __name__ == '__main__':
    ans = main()
    print(ans)
