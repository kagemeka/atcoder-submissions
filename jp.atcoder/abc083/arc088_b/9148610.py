import sys

s = sys.stdin.readline().rstrip()
n = len(s)

def main():
    m = n // 2
    if n & 1:
        l = s[m::-1]
        r = s[m:]
    else:
        l = s[m-1::-1]
        r = s[m:]
    base = l[0]

    cnt = m
    i = 0
    while i < m:
        if l[i] == r[i] == base:
            i += 1
            cnt += 1
        else:
            break
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
