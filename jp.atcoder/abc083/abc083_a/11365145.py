import sys

a, b, c, d = map(int, sys.stdin.readline().split())
l = a + b
r = c + d

def main():
    if l > r: ans = 'Left'
    elif l == r: ans = 'Balanced'
    else: ans = 'Right'
    print(ans)

if __name__ ==  '__main__':
    main()
