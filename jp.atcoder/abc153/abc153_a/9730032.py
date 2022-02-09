import sys

h, a = map(int, sys.stdin.readline().split())

def main():
    return (h + a - 1) // a

if __name__ == '__main__':
    ans = main()
    print(ans)
