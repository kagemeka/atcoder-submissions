import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    T = b / a
    A = d / c
    if T == A:
        return 'DRAW'
    elif T > A:
        return 'TAKAHASHI'
    else:
        return 'AOKI'

if __name__ == '__main__':
    ans = main()
    print(ans)
