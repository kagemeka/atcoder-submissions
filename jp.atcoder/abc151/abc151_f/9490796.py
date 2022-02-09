import sys
import cmath
from itertools import combinations

inf = float('inf')

n, *xy = map(int, sys.stdin.read().split())
xy = zip(*[iter(xy)] * 2)
z = [x + y*1j for x, y in xy]

def circumcenter(z1, z2, z3):
    a = z2 - z1
    b = z3 - z1
    numerator = a * b * (b.conjugate() - a.conjugate())
    denominator = a * b.conjugate() - a.conjugate() * b
    o = numerator / denominator
    r = abs(o)
    o += z1
    return o, r

def center(z1, z2):
    a = z2 - z1
    o = a / 2
    r = abs(o)
    o += z1
    return o, r

def main():
    cand = []
    for comb in combinations(z, 3):
        try:
            cand.append(circumcenter(*comb))
        except:
            pass
    for comb in combinations(z, 2):
        cand.append(center(*comb))

    res = inf
    for o, r in cand:
        r += r * 10 ** -6
        for i in z:
            if abs(i - o) > r:
                break
        else:
            res = min(res, r)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
