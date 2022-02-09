import sys

x = sys.stdin.readline().rstrip()

def main():
    return ord(x) - 64

if __name__ == '__main__':
    ans = main()
    print(ans)
