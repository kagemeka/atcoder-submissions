import sys

n = int(sys.stdin.readline().rstrip())

def main():
    return n * 2 if n & 1 else n

if __name__ == '__main__':
    ans = main()
    print(ans)
