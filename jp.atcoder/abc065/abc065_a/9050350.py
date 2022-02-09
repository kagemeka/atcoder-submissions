import sys

x, a, b = map(int, sys.stdin.readline().split())

def main():
    best = -b + a
    if best >= 0:
        return 'delicious'
    elif best >= -x:
        return 'safe'
    else:
        return 'dangerous'

if __name__ == '__main__':
    ans = main()
    print(ans)
