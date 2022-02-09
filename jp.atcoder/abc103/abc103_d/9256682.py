import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2))

def main():
    r = -1
    cnt = 0
    for a, b in ab:
        if a < r:
            if b < r:
                r = b
            continue
        else:
            cnt += 1
            r = b
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
