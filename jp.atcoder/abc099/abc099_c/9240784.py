import sys
from math import log, floor

n = int(sys.stdin.readline().rstrip())

def main():
    r = n
    cnt = 0
    while r >= 15 or 0 < r <= 11:
        p6, p9 = floor(log(r, 6)), floor(log(r, 9))
        r -= max(6 ** p6, 9 ** p9)
        cnt += 1
    if 12 <= r <= 14:
        q, s = divmod(r, 6)
        cnt += q + s

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
