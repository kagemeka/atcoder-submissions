import sys

n, x, *m = map(int, sys.stdin.read().split())

def main():
    remainder = x - sum(m)
    cnt = n
    cnt += remainder // min(m)
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
