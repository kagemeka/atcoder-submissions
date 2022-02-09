import sys

n, *p = map(int, sys.stdin.read().split())

def main():
    cnt = 0
    big = p[1] > p[0]
    for i in range(1, n-1):
        if big:
            cnt += 1 & (p[i] < p[i+1])
        else:
            cnt += 1 & (p[i] > p[i+1])

        big = p[i+1] > p[i]

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
