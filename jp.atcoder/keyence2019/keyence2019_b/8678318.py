# 2019-11-28 00:55:58(JST)
import sys
def main():
    s = sys.stdin.readline().rstrip()

    t = 'keyence'
    for i in range(8):
        if t[:i] == s[:i] and t[i:] == s[-(7-i):]:
            ans = 'YES'
            break
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
