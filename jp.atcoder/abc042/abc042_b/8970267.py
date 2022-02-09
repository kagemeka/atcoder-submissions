import sys

n, l, *s = sys.stdin.read().split()

def main():
    s.sort()
    t = ''.join(s)
    return t

if __name__ == '__main__':
    ans = main()
    print(ans)
