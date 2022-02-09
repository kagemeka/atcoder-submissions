import sys

n, *a = map(int, sys.stdin.read().split())

def main():
    cnt = 0
    for i in a:
        while not i % 2:
            i //= 2
            cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
