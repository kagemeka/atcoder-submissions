import sys

a, b = map(int, sys.stdin.readline().split())

def main(a, b):
    h = w = 100
    yield '{0} {1}'.format(h, w)

    if a >= b:
        c1 = '.'
        c2 = '#'
    else:
        a, b = b, a
        c1 = '#'
        c2 = '.'

    canvas = [[c2] * w for _ in range(h//2)] + [[c1] * w for _ in range(h//2)]
    a -= 1
    b -= 1

    i = 0
    j = 0
    while a:
        canvas[i][j] = c1
        a -= 1
        j += 2
        if j == 100:
            j = 0
            i += 2

    i = 51
    j = 0
    while b:
        canvas[i][j] = c2
        b -= 1
        j += 2
        if j == 100:
            j = 0
            i += 2

    for i in range(h):
        yield ''.join(canvas[i])

if __name__ == '__main__':
    ans = main(a, b)
    print(*ans, sep='\n')
