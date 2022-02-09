import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    h = 2
    w = max(a, b) * 2

    s1 = [None] * w
    if a >= b:
        c1 = '.'
        c2 = '#'
    else:
        c1 = '#'
        c2 = '.'

    m = min(a, b)
    for i in range(0, w, 2):
        s1[i] = c1
    for i in range(1, w, 2):
        s1[i] = c2

    s2 = s1.copy()
    for i in range(m * 2, w, 2):
        s2[i] = c2

    ans = ['{0} {1}'.format(h, w), ''.join(s1), ''.join(s2)]
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
