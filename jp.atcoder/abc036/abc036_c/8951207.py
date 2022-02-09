import sys

n, *a = map(int, sys.stdin.read().split())
a = sorted(enumerate(a), key=lambda x: x[1])

def main():
    cur = 0
    res = [None] * n
    prev = a[0][1]
    for i, v in a:
        if v != prev:
            cur += 1
        res[i] = cur
        prev = v

    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
