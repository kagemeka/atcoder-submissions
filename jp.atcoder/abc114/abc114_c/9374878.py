import sys
from itertools import product
from bisect import bisect_right as bi_r

shichigosan = set('357')

cand = []
for i in range(3, 10):
    for x in product('357', repeat=i):
        x = ''.join(x)
        if set(x) == shichigosan:
            cand.append(int(''.join(x)))

n = int(sys.stdin.readline().rstrip())

def main():
    return bi_r(cand, n)

if __name__ == '__main__':
    ans = main()
    print(ans)
