import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()
s += '0'

def main():
    l = [0]
    r = [0]
    flag = False
    for i in range(n+1):
        if s[i] == '1':
            if not flag:
                l.append(i)
            flag = True
        else:
            if flag:
                r.append(i-1)
            flag = False

    l.append(n-1)
    r.append(n-1)
    m = len(l)

    if k >= m - 1:
        return n
    res = 0
    for i in range(m-k):
        res = max(res, r[i+k]-l[i]+1)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
