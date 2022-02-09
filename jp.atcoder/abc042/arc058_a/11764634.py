import sys
from string import digits

n, k, *d = sys.stdin.read().split()
d = set(digits) - set(d)
l = len(n)

def main(d):
    res = ''
    flag = True
    for i in range(l):
        if flag:
            if n[i] in d:
                res += n[i]
            else:
                flag = False
                for j in range(int(n[i]), 10):
                    if str(j) in d:
                        res += str(j)
                        break
                else:
                    break
        else:
            res += min(d)
    else:
        print(res)
        return
    d = sorted(d)
    res = d[0] * (l + 1) if d[0] != '0' else d[1] + '0' * l
    print(res)

if __name__ ==  '__main__':
    main(d)
