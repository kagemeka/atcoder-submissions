import sys

x = map(int, list(sys.stdin.readline().rstrip()))

def main():
    return sum(x)

if __name__ == '__main__':
    ans = main()
    print(ans)
