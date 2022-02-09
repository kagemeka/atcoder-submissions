import sys

s = sys.stdin.readline().rstrip().split(',')

def main():
    return s

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
