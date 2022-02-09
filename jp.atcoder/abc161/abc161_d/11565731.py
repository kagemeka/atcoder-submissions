import sys
from string import digits

k = int(sys.stdin.readline().rstrip())

def main():
    if k <= 9:
        print(k)
        return
    res = list(digits[1:])
    r = k - 9
    while True:
        nex = []
        for n in res:
            o = ord(n[-1])
            for i in range(-1, 2):
                d = chr(o + i)
                if d < '0' or d > '9': continue
                nex.append(n + d)
                r -= 1
                if not r:
                    print(nex[-1])
                    return
        res = nex.copy()

if __name__ ==  '__main__':
    main()
