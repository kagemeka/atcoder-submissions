import sys
from itertools import accumulate

res = [0] * (10 ** 6 + 2)

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = map(int, sys.stdin.read().split())
    ab = zip(ab, ab)

    # いもす法
    for a, b in ab:
        res[a] += 1
        res[b+1] -= 1

    ans = max(accumulate(res))
    print(ans)

if __name__ == '__main__':
    main()
