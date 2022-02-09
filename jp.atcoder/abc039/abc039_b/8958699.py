import sys

x = int(sys.stdin.readline().rstrip())

def main():
    ans = x ** (1 / 4)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
