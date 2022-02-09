import sys

x = int(sys.stdin.readline().rstrip())

def main():
    return 'ABC' if x < 1200 else 'ARC'

if __name__ == '__main__':
    ans = main()
    print(ans)
