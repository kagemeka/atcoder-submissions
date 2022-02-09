import sys
from itertools import combinations

s = list(sys.stdin.readline().rstrip())
l = len(s)

def main():
    res = 0
    cand = range(1, l)
    for inser_cnt in range(l):
        for idces in combinations(cand, inser_cnt):
            t = s.copy()
            idces = list(idces)
            for i in idces[::-1]:
                t.insert(i, '+')
            res += eval(''.join(t))

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
