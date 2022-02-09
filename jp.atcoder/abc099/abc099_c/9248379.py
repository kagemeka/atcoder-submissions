import sys
from math import log, floor

n = int(sys.stdin.readline().rstrip())

def main():
    cand = set()
    for i in range(floor(log(n, 6)) + 1):
        if 6 ** i <= n:
            cand.add(6 ** i)
        if 9 ** i <= n:
            cand.add(9 ** i)
    cand = sorted(cand)

    res = set([0])
    cnt = 0
    while True:
        nex = set()
        for val in res:
            for c in cand:
                if val + c <= n:
                    nex.add(val + c)
                else:
                    break
        cnt += 1
        if n in nex:
            return cnt
        res = nex

if __name__ == '__main__':
    ans = main()
    print(ans)
