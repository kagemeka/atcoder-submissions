import sys

s = sys.stdin.readline().rstrip() + '.'

def main():
    l = len(s)
    t = ''
    cnt = 1
    for i in range(1, l):
        if s[i] != s[i-1]:
            t += s[i-1] + str(cnt)
            cnt = 1
        else:
            cnt += 1
    return t

if __name__ == '__main__':
    ans = main()
    print(ans)
