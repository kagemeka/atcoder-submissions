import sys
from itertools import product

s = sys.stdin.readline().rstrip()

def main():
    for ops in product('+-', repeat=3):
        res = s[0]
        for i in range(3):
            res += ops[i] + s[i+1]
        if eval(res) == 7:
            print(res + '=7')
            return

if __name__ ==  '__main__':
    main()
