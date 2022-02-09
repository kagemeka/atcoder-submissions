# 2019-11-26 17:11:55(JST)
import sys
def main():
    s = sys.stdin.readline().rstrip()
    ans = s[:4] + ' ' + s[4:]
    print(ans)

if __name__ == '__main__':
    main()
