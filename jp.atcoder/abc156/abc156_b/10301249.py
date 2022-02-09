import sys

n, k = map(int, sys.stdin.readline().split())

def main():
    cnt = 1
    m = 1
    while m <= n:
        m *= k
        cnt += 1
    return cnt - 1

if __name__ == '__main__':
    ans = main()
    print(ans)
