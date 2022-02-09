import sys

r = map(int, sys.stdin.readline().rstrip())

def main():
    if r < 1200:
        return 'ABC'
    elif r < 2800:
        return 'ARC'
    else:
        return 'AGC'

if __name__ == '__main__':
    ans = main()
    print(ans)
