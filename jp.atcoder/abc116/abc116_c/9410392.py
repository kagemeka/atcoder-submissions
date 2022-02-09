import sys

n, *h = map(int, sys.stdin.read().split())

def main():
    cnt = 0

    for _ in range(max(h)):
        prev_0 = True
        for i in range(n):
            if h[i] > 0:
                h[i] -= 1
                if prev_0:
                    cnt += 1
                    prev_0 = False
            else:
                prev_0 = True

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
