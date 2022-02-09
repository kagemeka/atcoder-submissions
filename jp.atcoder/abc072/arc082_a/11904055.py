import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    m = 10 ** 5
    cnt = [0] * (m + 1)
    for x in a:
        cnt[x] += 1
        if x > 0: cnt[x-1] += 1
        if x < m: cnt[x+1] += 1
    print(max(cnt))

if __name__ ==  '__main__':
    main()
