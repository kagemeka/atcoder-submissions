import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def main():
    cnt_seq = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt_seq += 1

    res = n - cnt_seq
    r = k
    the_other = dict([('L', 'R'), ('R', 'L')])
    a = s[0]
    b = the_other[a]
    for i in range(1, n):
        if not r:
            break
        if s[i] == a and s[i-1] == b:
            res += 2
            r -= 1
    if s[-1] == b and r:
        res += 1

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
