import sys

def cnt(n):
    m = str(n)
    l = len(m)
    if l == 1: return n + 1
    tot = 0
    tot += pow(10, (l - 1) // 2) * (int(m[0]) - 1)
    tot += pow(10, l // 2) - 1 - pow(10, l // 2 - 1) * (l & 1 ^ 1)
    while l >= 2:
        l -= 2
        if l == 0: tot += m[1] >= m[0]
        elif l == 1: tot += int(m[1]) + 1 - (m[-1] < m[0])
        else:
            m = str(int(m[1:-1]) - (m[-1] < m[0]))
            m = '0' * (l - len(m)) + m
            tot += int(m[0]) * pow(10, (l - 1) // 2)
    return tot

a, b = map(int, sys.stdin.readline().split())

def main():
    print(cnt(b) - cnt(a-1))

if __name__ ==  '__main__':
    main()
