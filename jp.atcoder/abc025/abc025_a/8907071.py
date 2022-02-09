import sys

s, n = sys.stdin.read().split()
n = int(n)

def main():
    q, r = divmod(n-1, 5)
    return s[q] + s[r]

if __name__ == '__main__':
    ans = main()
    print(ans)
