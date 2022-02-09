import sys

cand = set('atcoder')

s, t = sys.stdin.read().split()
n = len(s)

def main():
    for i in range(n):
        c = s[i]
        d = t[i]
        if c == d:
            continue
        if (c == '@' and d in cand) or (d == '@' and c in cand):
            continue
        return 'You will lose'
    return 'You can win'

if __name__ == '__main__':
    ans = main()
    print(ans)
