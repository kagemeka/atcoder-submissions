import sys

x, y = sys.stdin.readline().split()

def main():
    if x < y: ans = '<'
    elif x == y: ans = '='
    else: ans = '>'
    print(ans)

if __name__ ==  '__main__':
    main()
