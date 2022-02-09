import sys

r = int(sys.stdin.readline().rstrip())

def main():
    if r < 1200: ans = 'ABC'
    elif r < 2800: ans = 'ARC'
    else: ans = 'AGC'
    print(ans)

if __name__ ==  '__main__':
    main()
