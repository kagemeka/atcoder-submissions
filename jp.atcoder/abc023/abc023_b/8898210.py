import sys

n, s = sys.stdin.read().split()
n = int(n)

def main():
    if n & 1 ^ 1:
        return -1

    if n % 3 == 0:
        a = s[::3]
        b = s[1::3]
        c = s[2::3]
    elif n % 3 == 1:
        b = s[::3]
        c = s[1::3]
        a = s[2::3]
    else:
        c = s[::3]
        a = s[1::3]
        b = s[2::3]

    if set(a) - set(['a']) or set(b) - set(['b']) or set(c) - set('c'):
        return -1
    return n // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
