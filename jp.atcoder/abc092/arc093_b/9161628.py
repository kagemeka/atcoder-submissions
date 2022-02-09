import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    h = 2
    w = max(a, b) * 2

    s1 = [None] * w
    s2 = [None] * w

    if a >= b:
        c1 = '.'
        c2 = '#'
    else:
        c1 = '#'
        c2 = '.'

    m = min(a, b)
    for i in range(w):
        if i & 1 == 0:
            s1[i] = s2[i] = c1
        else:
            s1[i] = c2
            if i < m * 2:
                s2[i] = c2
            else:
                s2[i] = s2[i-1] = c2

    ans = ['{0} {1}'.format(h, w), ''.join(s1), ''.join(s2)]
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
