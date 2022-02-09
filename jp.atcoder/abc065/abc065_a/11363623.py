import sys

x, a, b = map(int, sys.stdin.readline().split())

def main():
    d = -a + b
    if d <= 0: ans = 'delicious'
    elif d <= x: ans = 'safe'
    else: ans = 'dangerous'
    print(ans)

if __name__ ==  '__main__':
    main()
