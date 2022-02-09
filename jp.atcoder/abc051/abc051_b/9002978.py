import sys

k, s = map(int, sys.stdin.readline().split())

def main():
    cnt = 0
    for x in range(min(s, k) + 1):
        t = s - x
        if 0 <= t <= k:
            cnt += t + 1
        elif k < t <= k * 2:
            cnt += k + 1 - (t - k)
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
