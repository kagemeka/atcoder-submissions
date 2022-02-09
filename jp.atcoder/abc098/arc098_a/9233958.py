import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

def main():
    l = 0
    r = s.count('E')
    res = r
    for i in range(n):
        cur = s[i]
        if cur == 'E':
            r -= 1
        res = min(res, l + r)
        if cur == 'W':
            l += 1
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
