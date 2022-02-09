import sys

n, *p = map(int, sys.stdin.read().split())


def main():
    cnt = 0
    for i in range(n):
        if p[i] != i + 1:
            cnt += 1

    if not cnt or cnt == 2:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
