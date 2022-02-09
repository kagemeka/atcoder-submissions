import sys

def fill(s): return '0' * (6 - len(s)) + s
def create_id(p, o): return fill(str(p)) + fill(str(o))

n, m, *py = map(int, sys.stdin.read().split())
pyi = sorted(zip(*[iter(py)] * 2 + [range(m)]))

def main():
    res = [None] * m
    prev = j = None
    for p, y, i in pyi:
        j = j + 1 if p == prev else 1
        res[i] = create_id(p, j)
        prev = p
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
