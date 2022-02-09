import sys

n, *H = map(int, sys.stdin.read().split())

def main():
    res = 0
    cnt = 0
    prev = 0
    for h in H + [float('inf')]:
        if h <= prev:
            cnt += 1
        else:
            res = max(res, cnt)
            cnt = 0
        prev = h
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
