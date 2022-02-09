import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    e = b / a
    f = c / d
    if e > f: ans = 'TAKAHASHI'
    elif e == f: ans = 'DRAW'
    else: ans = 'AOKI'
    print(ans)

if __name__ ==  '__main__':
    main()
