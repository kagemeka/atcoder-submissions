import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    res = set()
    for i in range(n):
        while not a[i] & 1:
            a[i] //= 2
        res.add(a[i])

    return len(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
