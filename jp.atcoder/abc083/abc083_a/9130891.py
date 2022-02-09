import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def main():
    l = a + b
    r = c + d
    if l > r:
        return 'Left'
    elif l == r:
        return 'Balanced'
    else:
        return 'Right'

if __name__ == '__main__':
    ans = main()
    print(ans)
