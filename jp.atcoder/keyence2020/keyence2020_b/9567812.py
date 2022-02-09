import sys

n, *xl = map(int, sys.stdin.read().split())
xl = sorted(zip(*[iter(xl)] * 2))

def main():
    cnt = 0
    cur = -float('inf')
    for x, l in xl:
        left = x - l
        right = x + l
        if left >= cur:
            cur = right
            cnt += 1
            continue
        else:
            if right > cur:
                pass
            else:
                cur = right
                continue

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
