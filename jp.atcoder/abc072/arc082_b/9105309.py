import sys

n, *p = map(int, sys.stdin.read().split())
p = [None] + p + [None]

def main():
    cnt = 0
    i = 0
    while i <= n:
        if p[i] == i:
            cnt += 1
            if p[i+1] == i + 1:
                i += 1
        i += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
