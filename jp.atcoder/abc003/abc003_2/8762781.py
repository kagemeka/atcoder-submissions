import sys

atcoder = set('atcoder')
s, t = sys.stdin.read().split()
n = len(s)

def main():

    for i in range(n):
        c1 = s[i]
        c2 = t[i]
        if c1 == c2:
            continue
        if c1 == '@' and c2 in atcoder:
            continue
        if c2 == '@' and c1 in atcoder:
            continue
        ans = 'You will lose'
        break
    else:
        ans = 'You can win'

    print(ans)

if __name__ == '__main__':
    main()
