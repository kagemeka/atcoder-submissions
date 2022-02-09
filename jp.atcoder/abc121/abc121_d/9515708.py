import sys

def cumxor(n):
    q, r = divmod(n+1, 2)
    return q & 1 ^ (n * r)

a, b = map(int, sys.stdin.readline().split())

def main():
    return cumxor(b) ^ cumxor(a-1)

if __name__ == '__main__':
    ans = main()
    print(ans)
