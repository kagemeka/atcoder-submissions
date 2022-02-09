import sys

o, e = sys.stdin.read().split()

def main():
    s = [None] * (len(o) + len(e))
    s[::2] = list(o)
    s[1::2] = list(e)
    return ''.join(s)

if __name__ == '__main__':
    ans = main()
    print(ans)
