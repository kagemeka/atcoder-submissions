import sys

r, g, b = sys.stdin.readline().split()

def main():
    ans = 'YES' if not int(g + b) % 4 else 'NO'
    print(ans)

if __name__ ==  '__main__':
    main()
