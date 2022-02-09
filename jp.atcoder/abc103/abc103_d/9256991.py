import sys

n, m, *ab = map(int, sys.stdin.read().split())
ab = sorted(zip(*[iter(ab)] * 2))

def main():
    r = ab[0][1]
    cnt = 0
    for a, b in ab[1:]:
        if a < r:
            if b < r:
                r = b
            continue
        else:
            cnt += 1
            r = b
    cnt += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
