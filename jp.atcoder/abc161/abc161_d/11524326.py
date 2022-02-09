import sys
from string import digits

k = int(sys.stdin.readline().rstrip())

def main():
    r = k
    if r <= 9:
        print(digits[r])
        return
    res = list(digits[1:])
    r -= 9
    d = set(digits)
    while True:
        nex = []
        for n in res:
            o = ord(n[-1])
            for i in range(-1, 2):
                tail = chr(o+i)
                if tail in d:
                    nex.append(n+tail)
                    r -= 1
                    if r == 0:
                        print(nex[-1])
                        return
        res = nex.copy()

if __name__ ==  '__main__':
    main()
