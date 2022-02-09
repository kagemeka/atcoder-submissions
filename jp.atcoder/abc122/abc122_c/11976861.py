import sys

n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
lr = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    cnt = [0] * n
    for i in range(n - 1):
        cnt[i+1] = s[i:i+2] == 'AC'
    for i in range(n - 1): cnt[i+1] += cnt[i]
    for l, r in lr:
        print(cnt[r-1] - cnt[l-1])

if __name__ ==  '__main__':
    main()
