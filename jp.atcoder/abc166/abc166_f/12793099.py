import sys

n, a, b, c = map(int, sys.stdin.readline().split())
s = sys.stdin.read().split() + ['$$']

def main(a, b, c):
    res = []
    for i in range(n):
        x, y = s[i], s[i+1]
        if x == 'AB':
            if a == b == 0: break
            if a > b:
                a -= 1
                b += 1
                res.append('B')
            elif a < b:
                a += 1
                b -= 1
                res.append('A')
            else:
                if y == 'AC':
                    a += 1
                    b -= 1
                    res.append('A')
                else:
                    a -= 1
                    b += 1
                    res.append('B')
        elif x == 'AC':
            if a == c == 0: break
            if a > c:
                a -= 1
                c += 1
                res.append('C')
            elif a < c:
                a += 1
                c -= 1
                res.append('A')
            else:
                if y == 'AB':
                    a += 1
                    b -= 1
                    res.append('A')
                else:
                    a -= 1
                    b += 1
                    res.append('C')
        elif x == 'BC':
            if b == c == 0: break
            if b > c:
                b -= 1
                c += 1
                res.append('C')
            elif b < c:
                b += 1
                c -= 1
                res.append('B')
            else:
                if y == 'AB':
                    b += 1
                    c -= 1
                    res.append('B')
                else:
                    b -= 1
                    c += 1
                    res.append('C')
    else:
        print('Yes')
        print(*res, sep='\n')
        return
    print('No')

if __name__ == '__main__':
    main(a, b, c)
