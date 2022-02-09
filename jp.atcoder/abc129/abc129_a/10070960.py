import sys

p, q, r = map(int, sys.stdin.readline().split())

def main():
    tot = p + q + r
    return tot - max(p, q, r)

if __name__ == '__main__':
    ans = main()
    print(ans)
