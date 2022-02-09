# 2019-11-22 19:46:21(JST)
import sys


def main():
    n, a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    s =  '#' + sys.stdin.readline().rstrip()
    if '##' in s[a+1:max(c, d)-1]:
        ans = 'No'
    else:
        # そうでなければFnukeはどこでもいける
        # '...'があればSnukeが追い越すことも可能
        if c < d:
            ans = 'Yes'
        elif c > d:
            if '...' in s[b-1:d]:
                ans = 'Yes'
            else:
                ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()
