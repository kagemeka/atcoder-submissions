import sys
from itertools import product

ops = '+-'

s = sys.stdin.readline().rstrip()

def main():
    formula = [None] * 7
    formula[::2] = list(s)

    for op in product(ops, repeat=3):
        f = formula.copy()
        f[1::2] = list(op)
        f = ''.join(f)
        if eval(f) == 7:
            return f + '=7'

if __name__ == '__main__':
    ans = main()
    print(ans)
