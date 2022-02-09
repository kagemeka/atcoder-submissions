import sys

sx, sy, tx, ty = map(int, sys.stdin.readline().split())

def main():
    dx = tx - sx + 1
    dy = ty - sy + 1
    u, r, d, l = list('URDL')

    res = ''
    res += u * (dy - 1)
    res += r * dx
    res += d * dy
    res += l * dx
    res += u + l
    res += u * dy
    res += r * dx
    res += d * dy
    res += l * (dx - 1)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
