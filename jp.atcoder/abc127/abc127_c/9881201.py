import sys

n, m, *lr = map(int, sys.stdin.read().split())
lr = zip(*[iter(lr)] * 2)

def main():
    le, ra = 1, n
    for l, r in lr:
        le = max(l, le)
        ra = min(r, ra)
    return ra - le + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
