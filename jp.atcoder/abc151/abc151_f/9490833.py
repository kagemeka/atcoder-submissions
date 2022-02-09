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
    o = numerator / denominator + z1
    return o

def center(z1, z2):
    return (z1 + z2) / 2

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
    for o in cand:
        r = 0
        for i in z:
            r = max(r, abs(o - i))
        res = min(res, r)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
