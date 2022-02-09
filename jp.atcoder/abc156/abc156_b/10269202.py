import sys

def base_convert(n, b):
    res = ''
    q = n
    while q:
        q, r = divmod(q, b)
        if r < 0:
            q += 1
            r -= b
        res = str(r) + res

    return int(res) if res else 0

n, k = map(int, sys.stdin.readline().split())

def main():
    return len(str(base_convert(n, k)))

if __name__ == '__main__':
    ans = main()
    print(ans)
