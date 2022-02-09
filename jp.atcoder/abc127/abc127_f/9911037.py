import sys
from heapq import heappush, heappop, heappushpop

n = int(sys.stdin.readline().rstrip())
Q = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
def main():
    c = 0
    res = 0
    lo, hi = [], []
    m_x = None
    for q in Q:
        if len(q) == 3:
            a, b = q[1:]
            c += b
            if not lo:
                heappush(lo, -a)
                m_x = a
                continue
            if len(lo) == len(hi):
                l, r = -heappop(lo), heappop(hi)
                heappush(lo, -l)
                if a <= r:
                    heappush(lo, -a)
                    heappush(hi, r)
                    if a >= l:
                        m_x = a
                    else:
                        res += l - a
                else:
                    res += a - r
                    heappush(lo, -r)
                    heappush(hi, a)
                    m_x = r
            else:
                l = -heappop(lo)
                if a >= l:
                    heappush(lo, -l)
                    heappush(hi, a)
                else:
                    heappush(lo, -a)
                    heappush(hi, l)
                    m_x = a
                res += abs(l - a)
        else:
            yield m_x, res + c

if __name__ == '__main__':
    ans = main()
    for a in ans:
        print(*a, sep=' ')
