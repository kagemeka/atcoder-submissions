import sys

n, q = map(int, sys.stdin.readline().split())
s = '$' + sys.stdin.readline().rstrip()
lr = zip(*[map(int, sys.stdin.read().split())] * 2)

def main():
    res = [None] * (n + 1); res[0] = 0
    prev = '$'
    for i in range(1, n+1):
        res[i] = res[i-1]
        res[i] += (prev == 'A' and s[i] == 'C') & 1
        prev = s[i]

    for l, r in lr:
        yield res[r] - res[l]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
