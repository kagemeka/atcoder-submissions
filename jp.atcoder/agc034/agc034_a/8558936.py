# 2019-11-22 19:46:21(JST)
import sys


def main():
    n, a, b, c, d = [int(x) for x in sys.stdin.readline().split()]
    s =  sys.stdin.readline().rstrip()

    # if a < b < c < d or a < b < d < c:
    #     if '##' in s[a+1:max(c, d)-1]:
    #         print('No')
    #         sys.exit()
    # if a < c < b < d:
    #     if '##' in s[a+1:c-1] or '##' in s[b+1:d-1]:
    #         print('No')
    #         sys.exit()

    # if c < d:
    #     ans = 'Yes'
    # elif c > d:
    #     if '...' in s[b-1:d]:
    #         ans = 'Yes'
    #     else:
    #         ans = 'No'

    if a < b < c < d or a < b < d < c:
        if '##' in s[a:max(c-1, d-1)-1]:
            print('No')
            sys.exit()
    if a < c < b < d:
        if '##' in s[a:c-2] or '##' in s[b:d-2]:
            print('No')
            sys.exit()

    if c < d:
        ans = 'Yes'
    elif c > d:
        if '...' in s[b-2:d-1]:
            ans = 'Yes'
        else:
            ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()
