import sys

a, b = map(int, sys.stdin.readline().split())

canvas = [['#'] * 100 for _ in range(50)] + [['.'] * 100 for _ in range(50)]
a -= 1; b -= 1

def paint(color, cnt):
    if color == '.':
        i = j = 0
    else:
        i = 51; j = 0

    while cnt:
        canvas[i][j] = color
        cnt -= 1
        j += 2
        if j == 100:
            j = 0
            i += 2

def main(a, b):
    yield '100 100'

    paint('.', a)
    paint('#', b)

    for i in range(100):
        yield ''.join(canvas[i])

if __name__ == '__main__':
    ans = main(a, b)
    print(*ans, sep='\n')
